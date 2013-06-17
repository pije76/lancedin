from django.conf.urls.defaults import *

urlpatterns = patterns(
    'project.views',

    url(r'^$', 'project_category', name='project-category'),
    url(r'^(?P<slug>[-\w]+)/$', 'project_list', name='project-list'),
    url('^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', 'project_detail', name="project-detail"),
#    url(r'^(?P<category>[\w\-]+)/(?P<slug>[\w\-]+)/$', 'project_detail'),
#    url(r'^(?P<category>[-w]+)/(?P<slug>[-w]+)/$', 'project_detail', name='project-detail'),
#    url(r'^(?P<category>[a-zA-Z0-9_.-]+)/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'project_detail', name='project-detail'),

    (r'^create.*$', 'add'),
    (r'^edit/(?P<project_id>\d+)/$', 'edit'),
    url(r'^delete/(?P<project_id>\d+)/$', 'delete', name='delete'),

#   url(r"^add/$", "add_page",name="add"),
#   url(r"^(?P<full_slug>.*)/add/$", "add_page",name="add"),
#   url(r"^(?P<full_slug>.*)/edit/$", "edit_page",name="edit"),
#   url(r'^$', ListView.as_view(model=Category,template_name='index.html',context_object_name="webpages_list",),name='index'),
#   url(r"^(?P<full_slug>.*)/$", "category", name="category"),

#    url(r'detail/(?P<pk>\d+)', DetailView.as_view(model=Category), name="category_list",),
#    url(r'update/(?P<pk>\d+)', UpdateView.as_view(model=Category), name="category_update",),
#    url(r'create', CreateView.as_view(model=Category), name="category_create",),
#    url(r'list', ListView.as_view(model=Category), name="category_list",),
)


#urlpatterns = patterns(
#    'django.views.generic.list_detail',
#    url(r'^$', 'object_list', {'queryset': Category.objects.all()}),
#    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', {'queryset': Project.objects.all()}),
#)

#urlpatterns += patterns(
#    'django.views.generic.list_detail',
#    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="cms-story"),
#    url(r'^$', 'object_list', info_dict, name="cms-home"),
#)
