Custom Transpilers and template Definition
==========================================

If you don't like the default context of python, you can compose your own
transpiler for use with other languages.  Here is an example for C++. It uses
the context container that will be described below:

::

        class CppContext(ContextDefinition):
            default_name = CONTEXT.cpp.all

        class CppTemplate(TemplateDefinition):
            default_context_cls = CppContext

        class CppTranspiler(Transpiler):
            template_cls = CppTemplate

..

Jetbrains Context String Constants
==================================

The context values for various languages used by Jetbrains are highly irregular
and unpredictable, so a container class has been provided to ease their usage

Some languages have multiple contexts.  Their references are nested.
Here are nested (Python) and unnested (SQL) examples;

::

    from shortbus.constants import CONTEXT

    CONTEXT.python.all
    CONTEXT.sql

..

Context strings have been provided for the following languages:

::

    all 
    XSL
    Cucumber
    Coffee script
    HAML
    JSON
    SQL
    Twig
    Type Script
    Completion
    C
    CSS
    CPP
    Dart
    Groovy
    HTML
    Java
    JS
    Kotlin
    Vue
    PHP
    Python
    XML

..