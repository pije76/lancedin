from django.views.generic import *
from django.db.models import Count, Min, Sum, Avg
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.http import HttpResponse

import json

from models import Project, Category, Skill
from decorators import confirm_required

#from mptt.templatetags.mptt_tags import cache_tree_children
#from haystack.query import SearchQuerySet
from haystack.views import SearchView
from meta.views import Meta


# Create your views here.
def index(request):
#    meta = Meta(
#        title=project.title,
#        description=project.description,
#        keywords=project.keywords.split(','),
#    )
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def project_category(request):
    #qs = qs.filter(level__lt=2)
    #root_nodes = cache_tree_children(qs)
    #root_nodes.sort(key=lambda node: len(node.get_children()), reverse=True)

    #parentcategory = Category.objects.all()

    #qc = Category.objects.filter(title=title)
    #category = qc.get()
    #if category:
    #    qsc = category.get_children()
    #    sub_categories = qsc.get()

    #node = Category.objects.all()
    #node = Category.objects.get(parent=None)
    #parentcategory = Category.objects.add_related_count(Category.tree.root_nodes(), Project, 'category', 'count', cumulative=True)
    #parentcategory = Category.tree.all()
    #parentcategory = Category.tree.add_related_count(node.get_children(), Project, 'category', 'count')
    #parentcategory = Category.objects.add_related_count(node.get_children(), Project, 'category', 'count')
    parentcategory = Category.objects.all()
    #parentcategory = Category.objects.filter(parent__isnull=True)
    #parentcategory = Category.objects.all().annotate(count=Count('title'))
    #parentcategory = Project.objects.values('category').annotate(count=Count('category'))
    #parentcategory = Category.objects.all().annotate(count=Count('title')).filter(parent__isnull=False)
    return render_to_response('project/project_category.html', locals(), context_instance=RequestContext(request))


def project_list(request, slug):
    #category = get_object_or_404(Category, slug=slug)  # Given a category slug, display all items in a category.
    category = get_object_or_404(Category, slug=slug)
    #category = Category.objects.filter(parent__isnull=True)
    projectlist = Project.objects.filter(category=category)
    return render_to_response("project/project_list.html", locals(), context_instance=RequestContext(request))

def project_detail(request, slug, category):
    category = Category.objects.filter(slug=category)
    projectdetail = Project.objects.filter(slug=slug)
    return render_to_response('project/project_detail.html', locals(),  context_instance=RequestContext(request))
#    return object_list(request, queryset=Category.objects.all(), paginate_by=20, template_name='project/project_list.html', extra_context={'category': category})


#class ProjectForm(forms.ModelForm):
#    class Meta:
#        model = Project
#        exclude = ['create_date', 'slug']

@login_required
def add(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            addproject = form.save(commit=False)
            addproject.user = request.user
            addproject.save()
        return HttpResponseRedirect(addproject.get_absolute_url())
    return render_to_response('project/project_add.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        editproject = form.save(commit=False)
        editproject.user = request.user
        editproject.save()
        return HttpResponseRedirect(editproject.get_absolute_url())
    return render_to_response('project/project_edit.html', {'project': project, 'form': form}, context_instance=RequestContext(request))


@login_required
def delete_confirm(request, project_id):
    project = Project.objects.get(pk=project_id)
    return RequestContext(request, {'project': project})


@confirm_required('project/confirm_delete.html', delete_confirm)
def delete(request, project_id):
    delete = Project.objects.get(pk=project_id)
    delete.delete()
    return HttpResponseRedirect('/myproject/')


#def project_search(request):
#    results = SearchQuerySet().autocomplete(request.GET.get('q', ''))  # Django-Haystack 1.x with Ajax Autocomplete
#    results = SearchQuerySet().auto_query(request.GET.get('q', ''))  # Django-Haystack 2.x with Ajax Autocomplete
#    return HttpResponse(json.dumps(results[:5]), content_type='application/json')

#def search(req):
#    return SearchView(template='search/search.html')(req)
