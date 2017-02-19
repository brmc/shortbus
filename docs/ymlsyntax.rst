===================
YML Template Syntax
===================

The shortbus yml syntax allows you to write abbreviations in a simplified format
by using sensible defaults

For example, the full xml template definition for mauto looks like this:

.. code-block:: xml

        <template name="mauto" toReformat="false" toShortenFQNames="true" value="$VAR1$ = models.AutoField($VAR2$)">
            <variable alwaysStopAt="true" defaultValue="&quot;FIELDNAME&quot;" expression="" name="VAR1"/>
            <variable alwaysStopAt="true" defaultValue="" expression="" name="VAR2"/>
            <context>
                <option name="Python" value="true"/>
            </context>
        </template>

This is how you would define it in yml:

.. code-block:: yml

        - name: mauto
          raw: $:FIELDNAME$ = models.AutoField($$)


Variable names follow the convention: ``$<variable name>:<default value>$`` where
either and/or both are optional.

If no variable name is given, a generic name
will be generated for each anonymous variable. They follow the pattern ``VAR<index + 1>``
and don't care about you or your dreams, so if you creatively name your variables
VAR1, VAR2, etc, you run the risk of screwing things up. I doubt I will try to
do anything about this, so if it's important to you, feel free to override
TemplateDefinition.variable_prefix

The point is all of the following are valid and produce the same results:

.. code-block:: python

        $VAR1:FIELDNAME$ = models.AutoField($VAR2$)
        $:FIELDNAME$ = models.AutoField($VAR2:$)
        $1:FIELDNAME$ = models.AutoField($:$)
        $VAR1:FIELDNAME$ = models.AutoField($$)

However if you don't like the default values, you can still drop down and
explicitly define each attribute. Here's the full example:

.. code-block:: yml

        - name: mauto
          raw: $VAR1$ = models.AutoField($VAR2$)
          toShortenFQNames: True
          toReformat: True
          variables:
            - name: VAR1
              defaultValue: FIELDNAME
              alwaysStopAt: True
              Expression: ''
            - name: VAR2
              defaultValue: ''
              alwaysStopAt: True
              Expression: ''
          context:
            - name: Python
              value: True


A couple notes:

- Most attributes map directly to their xml counterparts with the exception of ``raw`` and ``template``. They are different ways to provide the value attribute on of your template.
- ``raw`` is intended to be used for simple, one-line pieces of code. It has precedence over ``template``.
- ``template`` is intended for multi-line code. It is the path of a file
- Quotation marks are not needed and should not be used except for empty values
- The yml file is a list, so multiple related definitions should be placed in the same file, unlike in SublimeText that uses one file per snippet
- Variable default values defined explicitly in the ``variables`` section and supersede implicit definitions in raw or template

