from django.conf import settings
from django import template
from classytags.core import Tag, Options
from classytags.arguments import Argument, Flag

register = template.Library()


class TryTag(Tag):
    name = 'try'
    options = Options(
        Flag('always', true_values=['true', 'yes'], default='no'),
        blocks=[('except', 'pre_except'), ('endtry', 'post_except')]
    )

    
    def render_tag(self, context, always, pre_except, post_except):
        context.push()
        if always or settings.DEBUG:
            try:
                r = pre_except.render(context)
            except Exception as e:
                r = post_except.render(context)
        else:
            r = pre_except.render(context)    
        context.pop()
        return r
        
        
register.tag(TryTag)
