=====
Usage
=====

Shortbus can import abbreviation definitions from three sources:

- Jetbrains live template XML
- SublimeText snippet XML, and
- a simplified custom YML format

And export to (currently) two formats:

- Jetbrains XML and
- the custom YML

Support for exporting to SublimeText will be implemented shortly

To get started, instantiate the Transpiler with a string to be used for the name.
In jetbrains this will be the group name where the live templates can be
found in the settings.

::

    from shortbus import Transpiler

    transpiler = Transpiler('Shortbus Templates')
..


From there, usage is pretty straight-forward. Each import method takes a single
argument. For Jetbrains XML and Shortbus YML, this is a file path, but
due to how SublimeText organizes snippets, it can be either a file or directory.

The API is fluent, so you can chain the calls:

::

    transpilers.import_from_yml('./my.yml')
        .import_from_sublimetext('~/path/to/sublimetext/snippetdir/)
        .import_from_jetbrains('~/.PyCharm2016.3/config/liveTemplates/Djaneiro.xml')
        .export_to_jetbrains('shortbus.xml')
        .export_to_yml('shortbus.yml')

..

