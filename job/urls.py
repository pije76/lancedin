from django.conf.urls.defaults import *

urlpatterns = patterns(
    'job.views',

    url(r'^$', 'job_category', name='job-category'),
    url(r'^(?P<slug>[-\w]+)/$', 'job_list', name='job-list'),
    url('^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', 'job_detail', name="job-detail"),
#    url(r'^(?P<category>[\w\-]+)/(?P<slug>[\w\-]+)/$', 'job_detail'),
#    url(r'^(?P<category>[-w]+)/(?P<slug>[-w]+)/$', 'job_detail', name='job-detail'),
#    url(r'^(?P<category>[a-zA-Z0-9_.-]+)/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'job_detail', name='job-detail'),

#    (r'^create.*$', 'edit'),
#    (r'^edit/(?P<job_id>\d+)/$', 'edit'),
#    (r'^delete/(?P<job_id>\d+)/$', 'delete'),

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
#    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', {'queryset': Job.objects.all()}),
#)

#urlpatterns += patterns(
#    'django.views.generic.list_detail',
#    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="cms-story"),
#    url(r'^$', 'object_list', info_dict, name="cms-home"),
#)
