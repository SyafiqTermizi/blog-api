import arrow

from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def moment(time):
    if time:
        return arrow.get(time).humanize()
    return None
