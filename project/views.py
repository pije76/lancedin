from django.views.generic import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse

import json

from models import Project, Category

#from mptt.templatetags.mptt_tags import cache_tree_children
#from haystack.query import SearchQuerySet


# Create your views here.
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def project_category(request):
    #qs = qs.filter(level__lt=2)
    #root_nodes = cache_tree_children(qs)
    #root_nodes.sort(key=lambda node: len(node.get_children()), reverse=True)

    #projectcategory = Category.objects.all()

    #qc = Category.objects.filter(title=title)
    #category = qc.get()
    #if category:
    #    qsc = category.get_children()
    #    sub_categories = qsc.get()

    #projectcategory = Category.objects.add_related_count(Category.tree.root_nodes(), Category, 'title', 'count', cumulative=True)
    #node = Category.objects.all()
    #projectcategory = Category.objects.add_related_count(node.get_children(), Category, 'title', 'count')

    #node = Category.objects.get(id=1)
    #projectcategory = Category.tree.all()
    #projectcategory = Category.tree.add_related_count(node.get_children(), Category, "parent", "count", cumulative=True)
    #projectcategory = Category.objects.add_related_count(node.get_children(), Project, 'category', 'count', True)
    projectcategory = Category.tree.add_related_count(Category.objects.all(), Category, 'title', 'count', cumulative=True)
    return render_to_response('project/project_category.html', locals(), context_instance=RequestContext(request))


def project_list(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Given a category slug, display all items in a category.
    projectlist = Project.objects.filter(category=category)
    return render_to_response("project/project_list.html", locals(), context_instance=RequestContext(request))


def project_detail(request, slug, category):
    category = Category.objects.filter(slug=category)
    projectdetail = Project.objects.filter(slug=slug)
    return render_to_response('project/project_detail.html', locals(),  context_instance=RequestContext(request))
#    return object_list(request, queryset=Category.objects.all(), paginate_by=20, template_name='project/project_list.html', extra_context={'category': category})


#def project_search(request):
#    results = SearchQuerySet().autocomplete(request.GET.get('q', ''))  # Django-Haystack 1.x with Ajax Autocomplete
#    results = SearchQuerySet().auto_query(request.GET.get('q', ''))  # Django-Haystack 2.x with Ajax Autocomplete
#    return HttpResponse(json.dumps(results[:5]), content_type='application/json')
