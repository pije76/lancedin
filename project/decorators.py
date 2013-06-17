# -*- coding: utf-8 -*-
# Code taken from Djangosnippets.org (http://djangosnippets.org/snippets/1922/)
 
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps
 
from django.shortcuts import render_to_response
from django.template import RequestContext

def confirm_required(template_name, context_creator, key='__confirm__'):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if request.POST.has_key(key):
                return func(request, *args, **kwargs)
            else:
                context = context_creator and context_creator(request, *args, **kwargs) or RequestContext(request)
                return render_to_response(template_name, context)
        return wraps(func)(inner)
    return decorator