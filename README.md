# django-trytag
A simple try...except tag for debugging and bodging Django templates.

Sometimes, to get your chickens and eggs in order, you need to suppress Django template errors...

## Usage
Add `trytag` to your installed apps.

Wrap your code in `{% try %} this {% except %} that {% endtry %}`. If `this` fails, `that` will be the output. Without the `{% except %}` block, it will fail silently.

By default, the try tag only has an effect if `settings.DEBUG` is `TRUE`. To make it happen all the time use `{% try always %}...{% endtry %}`.

## Requirements
Classy Tags: https://github.com/ojii/django-classy-tags
```
pip install django-classy-tags
```
