#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import glob
import os
import warnings

from lxml import etree as ElementTree
from yaml import load, dump

from shortbus.components import warn_if_missing_templates, TemplateDefinition

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Transpiler(object):
    def __init__(self, name: str = "Template Group"):
        self.name = name
        self.templates = {}

    def import_from_yml(self, path: str):
        """
        :param path: to yml file
        :return:
        """

        if not os.path.isfile(path):
            warnings.warn('YML file not found: ' + path + '. Skipping')
            return

        stream = open(path)
        data = load(stream, Loader=Loader)
        stream.close()

        if data is None:
            warnings.warn('YML File is empty or has invalid data:'
                          + path + '. Skipping')
            return

        templates = [TemplateDefinition.build_from_yml(x) for x in data]

        templates.sort(key=lambda x: x.name.lower())

        templates = {template.name: template for template in templates}

        self.templates.update(templates)

        return self

    def import_from_sublimetext(self, file_or_dir_path: str) -> 'Transpiler':
        """
        :param file_or_dir_path: either to a specific file, or a directory
        with multiple
        snippets
        """

        if os.path.isdir(file_or_dir_path):
            file_or_dir_path = os.path.join(file_or_dir_path,
                                            '**',
                                            '*.sublime-snippet')

        files = glob.glob(file_or_dir_path, recursive=True)

        xml = [ElementTree.parse(file).getroot() for file in files]

        templates = [TemplateDefinition.build_from_snippet(child)
                     for child in xml]

        templates.sort(key=lambda x: x.name.lower())
        templates = {template.name: template for template in templates}

        self.templates.update(templates)

        return self

    def import_from_jetbrains(self, file_path: str) -> 'Transpiler':
        """
        :param file_path:
        """

        xml = ElementTree.parse(file_path).getroot()
        self.name = xml.attrib['group']

        templates = [TemplateDefinition.build_from_xml(child)
                     for child in xml]
        templates.sort(key=lambda x: x.name.lower())
        templates = {template.name: template for template in templates}

        self.templates.update(templates)

        return self

    # @warn_if_missing_templates
    def export_to_jetbrains(self, output_path: str) -> 'Transpiler':
        template_set = ElementTree.Element('templateSet')
        template_set.attrib['group'] = self.name

        for key, template in self.templates.items():
            xml_template = ElementTree.SubElement(
                template_set,
                'template',
                template.to_jetbrains_dict())

            for key, var in template.variables.items():
                ElementTree.SubElement(
                    xml_template,
                    'variable',
                    var.to_jetbrains_dict())

            context = ElementTree.SubElement(xml_template, 'context')

            for option in template.context_options:
                ElementTree.SubElement(
                    context,
                    'option',
                    option.to_jetbrains_dict())

        tree = ElementTree.ElementTree(template_set)

        tree.write(output_path, pretty_print=True)

        return self

    @warn_if_missing_templates
    def export_to_yml(self, output_path: str) -> 'Transpiler':
        stream = open(output_path, 'w')
        tpls = [tpl.to_yml_dict() for tpl in self.templates.values()]
        dump(tpls, stream, Dumper=Dumper, default_flow_style=False)
        stream.close()

        return self
