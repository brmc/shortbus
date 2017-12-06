class Css:
    all = 'CSS',
    declaration = 'CSS_DECLARATION_BLOCK',
    property = 'CSS_PROPERTY_VALUE',
    ruleset = 'CSS_RULESET_LIST'


class Dart:
    all = 'DART'
    statement = 'DART_STATEMENT'
    top_level = 'DART_TOPLEVEL'


class Groovy:
    all = 'GROOVY'
    declaration = 'GROOVY_DECLARATION'
    expression = 'GROOVY_EXPRESSION'
    statement = 'GROOVY_STATEMENT'


class Html:
    all = 'HTML'
    text = 'HTML_TEXT'


class Java:
    all = 'JAVA_CODE'
    comment = 'JAVA_COMMENT'
    declaration = 'JAVA_DECLARATION'
    expression = 'JAVA_EXPRESSION'
    statement = 'JAVA_STATEMENT'
    string = 'JAVA_STRING'


class Js:
    all = 'JAVA_SCRIPT'
    jsx = 'JSX_HTML'
    expression = 'JS_EXPRESSION'
    statement = 'JS_STATEMENT'


class Kotlin:
    cls = 'KOTLIN_CLASS'
    comment = 'KOTLIN_COMMENT'
    expression = 'KOTLIN_EXPRESSION'
    obj_declaration = 'KOTLIN_OBJECT_DECLARATION'
    statement = 'KOTLIN_STATEMENT'
    top_level = 'KOTLIN_TOPLEVEL'


class C:
    all = 'c'
    declaration = 'OC_DECLARATION_C'
    expression = 'OC_EXPRESSION_C'
    statemnet = 'OC_STATEMENT_C'


class Cpp:
    all = 'cpp'
    declaration = 'OC_DECLARATION_CPP'
    expression = 'OC_EXPRESSION_CPP'
    statement = 'OC_STATEMENT_CPP'


class Php:
    all = 'PHP'
    class_member = 'PHP Class Member'
    comment = 'PHP Comment'
    expression = 'PHP Expression'
    statement = 'PHP Statement'
    string = 'PHP String Literal'


class Python:
    all = 'Python'
    django = 'Django'
    cls = 'Python_Class'


class Vue:
    all = 'Vue'
    component = 'VUE_COMPONENT_DESCRIPTOR'
    tag = 'VUE_INSIDE_TAG'
    script = 'VUE_SCRIPT'
    template = 'VUE_TEMPLATE'
    top_level = 'VUE_TOP_LEVEL'


class Xml:
    all = 'XML'
    text = 'XML_TEXT'


class ContextContainer:
    all = 'OTHER'
    xsl = 'XSL_TEXT'
    cucumber = 'CUCUMBER_FEATURE_FILE'
    coffee_script = 'CoffeeScript'
    haml = 'HAML'
    json = 'JSON'
    sql = 'SQL'
    twig = 'Twig'
    type_script = 'TypeScript'
    completion = 'COMPLETION'

    c = C
    css = Css
    cpp = Cpp
    dart = Dart
    groovy = Groovy
    html = Html
    java = Java
    js = Js
    kotlin = Kotlin
    vue = Vue
    php = Php
    python = Python
    xml = Xml


CONTEXT = ContextContainer
