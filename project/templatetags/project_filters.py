import re
import HTMLParser
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def removetags_hard(value):
    print "I'm removing tags now from:"
    print value
    """Removes Tags for HTML text"""
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', value)

@register.filter(is_safe=True)
@stringfilter
def addtags(value):
    h = HTMLParser.HTMLParser()
    return h.unescape(value)
 
