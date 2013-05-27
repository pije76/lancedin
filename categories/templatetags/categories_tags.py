import logging

from django import template
from categories.models import Category, CATEGORY_PUBLICY_PUBLIC

register = template.Library()

class GetCategoriesNode(template.Node):
    """
    Retrieves a set of category objects.

    Usage::

        {% get_categories 5 as varname %}

        {% get_categories 5 as varname asc %}

        {% get_categories 1 to 5 as varname %}

        {% get_categories 1 to 5 as varname asc %}
    """
    def __init__(self, varname, count=None, start=None, end=None, order='desc'):
        self.count = count
        self.start = start
        self.end = end
        self.order = order
        self.varname = varname.strip()

    def render(self, context):
        # determine the order to sort the categories
        """
        if self.order and self.order.lower() == 'desc':
            order = '-publish_date'
        else:
            order = 'publish_date'
        """

        #user = context.get('user', None)

        # get the categories in the appropriate order
        categories = Category.objects.filter(public=CATEGORY_PUBLICY_PUBLIC)#.order_by(order)

        if self.count:
            # if we have a number of categories to retrieve, pull the first of them
            categories = categories[:int(self.count)]
        else:
            # get a range of categories
            categories = categories[(int(self.start) - 1):int(self.end)]

        # don't send back a list when we really don't need/want one
        if len(categories) == 1 and not self.start and int(self.count) == 1:
            categories = categories[0]

        # put the article(s) into the context
        context[self.varname] = categories
        return ''



def get_categories(parser, token):
    """
    Retrieves a list of Categories objects for use in a template.
    """
    args = token.split_contents()
    argc = len(args)

    try:
        assert argc in (4,6) or (argc in (5,7) and args[-1].lower() in ('desc', 'asc'))
    except AssertionError:
        raise template.TemplateSyntaxError('Invalid get_categories syntax.')

    # determine what parameters to use
    order = 'desc'
    count = start = end = varname = None
    if argc == 4: t, count, a, varname = args
    elif argc == 5: t, count, a, varname, order = args
    elif argc == 6: t, start, t, end, a, varname = args
    elif argc == 7: t, start, t, end, a, varname, order = args

    return GetCategoriesNode(count=count,
                            start=start,
                            end=end,
                            order=order,
                            varname=varname)

# register the tags!
register.tag(get_categories)
