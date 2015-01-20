# django-trytag
A simple try...except tag for debugging and bodging Django templates.

Why would this be useful? I wrote this to stop `{% url ... %}` tags with missing urlconf entries from halting template rendering during development. It might be useful, should you find yourself in a similar situation.

Note to self: If you find yourself using this too much, you're probably doing it wrong.

## Usage
Add `trytag` to your installed apps.

Wrap your code in `{% try %} this {% except %} that {% endtry %}`. If `this` fails, `that` will be the output. Without the `{% except %}` block, it will fail silently.

By default, the try tag only has an effect if `settings.DEBUG` is `TRUE`. To make it happen all the time use `{% try always %}...{% endtry %}`.

## Requirements
Classy Tags: https://github.com/ojii/django-classy-tags
```
pip install django-classy-tags
```
