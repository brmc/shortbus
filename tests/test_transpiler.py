#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from unittest import TestCase
from xml.etree import ElementTree

from shortbus import Transpiler
from shortbus.components import VariableDefinition, TemplateDefinition, \
    ContextDefinition
from shortbus.constants import CONTEXT

try:
    from yaml import CLoader as Loader, CDumper as Dumper, dump
except ImportError:
    from yaml import Loader, Dumper


class GeneratorTest(TestCase):
    def setUp(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.valid_yml_path = os.path.join(
            self.directory, 'data', 'valid.yml')
        self.warning_yml_path = os.path.join(
            self.directory, 'data', 'warns.yml')
        self.jetbrains_xml = os.path.join(
            self.directory, 'data', 'jetbrains.xml')

        self.data_dir = os.path.join(self.directory, 'data')

        self.generator = Transpiler('Djaneiro: Models') \
            .import_from_yml(self.valid_yml_path)

        self.yml_templates = Transpiler().import_from_yml(
            self.valid_yml_path).templates

        self.xml_templates = Transpiler().import_from_jetbrains(
            self.jetbrains_xml).templates

    def tearDown(self):
        pass

    def test_default_values_for_template_and_raw(self):
        variables = {
            'var': VariableDefinition('var'),
            'end': VariableDefinition('end')
        }

        value = '$var$ = models.AutoField($var$)$end$'
        default = TemplateDefinition(
            name='raw',
            value=value,
            variables=variables,
        )

        template = self.yml_templates['raw']

        self.assertEqual(default, template)

        value = '$moo$\n$joo$'

        variables = {
            'moo': VariableDefinition('moo'),
            'joo': VariableDefinition('joo')
        }

        default.value = value
        default.variables = variables
        default.name = 'template'

        template = self.yml_templates['template']

        self.assertEqual(default, template)

    def test_variable_default_definitions(self):
        value = '$weep$ $graa:nah$ $weep:$ $:ni$ $ni$ $$'

        template = self.yml_templates['bah']
        variables = template.variables

        print(variables)

        self.assertEqual(variables['weep'].defaultValue, 'crabrabbit')
        self.assertEqual(variables['graa'].defaultValue, 'hard')
        self.assertEqual(variables['VAR4'].defaultValue, 'ni')
        self.assertEqual(variables['ni'].defaultValue, '')

        self.assertEqual(template.value,
                         '$weep$ $graa$ $weep$ $VAR4$ $ni$ $VAR6$')
        self.assertEqual(len(variables), 5)

    def test_variable_typo_throws_warning(self):
        with self.assertWarns(Warning):
            Transpiler().import_from_yml(self.warning_yml_path)

    def test_create_from_jetbrains_format(self):
        tpl = self.xml_templates['mauto']

        variables = {
            'VAR': VariableDefinition(name='VAR', defaultValue='FIELDNAME'),
            'VAR2': VariableDefinition(name='VAR2')
        }

        template = TemplateDefinition(
            name='mauto',
            value='$VAR$ = models.AutoField($VAR2$)',
            toReformat=False,
            toShortenFQNames=True,
            variables=variables
        )

        self.assertEqual(tpl.to_jetbrains_dict(), template.to_jetbrains_dict())

    def test_jetbrains_export(self):
        group = 'Djaneiro: Models'
        a = TemplateDefinition(
            name='mauto',
            value='$VAR$ = models.AutoField($VAR2$)',
            toReformat=False,
            toShortenFQNames=True,
            variables={
                'VAR': VariableDefinition('VAR', 'FIELDNAME'),
                'VAR2': VariableDefinition('VAR2')
            }
        )

        generator = Transpiler(group)
        generator.templates = {'mauto': a}

        path = os.path.join(self.data_dir, 'bullshit.xml')
        generator.export_to_jetbrains(path)

        a = ElementTree.parse(path).getroot()
        b = ElementTree.parse(self.jetbrains_xml).getroot()

        self.assertEqual(a.tag, b.tag)
        template_a, template_b = a.findall('template')[0], \
                                 b.findall('template')[0]
        self.assertEqual(sorted(template_a.items()),
                         sorted(template_b.items()))

        variables_a = template_a.findall('variable')
        variables_b = template_b.findall('variable')
        variables = zip(variables_a, variables_b)

        for a, b in variables:
            self.assertEqual(sorted(a.items()),
                             sorted(b.items()))

        options_a = template_a.find('context').findall('option')
        options_b = template_b.find('context').findall('option')

        options = zip(options_a, options_b)
        for a, b in options:
            self.assertEqual(sorted(a.items()),
                             sorted(b.items()))

    def test_import_from_sublime(self):
        a = Transpiler('test')
        path = os.path.join(self.data_dir)
        sublime = a.import_from_sublimetext(self.data_dir)

        path = os.path.join(self.data_dir, 'jetbrains.xml')
        jetbrains = a.import_from_jetbrains(path)

        self.assertEqual(jetbrains, sublime)

    def test_custom_transpiler(self):
        class CppContext(ContextDefinition):
            default_name = CONTEXT.cpp.all

        class CppTemplate(TemplateDefinition):
            default_context_cls = CppContext

        class CppTranspiler(Transpiler):
            template_cls = CppTemplate

        transpiler = CppTranspiler('cpp')

        path = os.path.join(self.data_dir, 'cpp.yml')
        transpiler.import_from_yml(path)
        result = transpiler.templates['bah'].context_options[0]
        self.assertEqual(result.name, 'cpp')

