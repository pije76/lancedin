from django import template
register = template.Library()
from django.conf import settings


@register.filter('read_more')
def read_more(description, absolute_url):
    if '<!--more-->' in description:
        return description[:description.find('<!--more-->')]+'<a href="'+str(absolute_url)+'">'+str(settings.READ_MORE_TEXT)+'</a>'
    else:
        return description

#def read_more(description, absolute_url):
#    pos = description.find('<!--more-->')
#    if pos == -1:
#        return description
#    else:
#        return '<a href="%s">%s</a>' % (description[:pos], settings.READ_MORE_TEXT))
