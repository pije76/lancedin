from django.conf.urls.defaults import *
from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse

from models import Profile
from views import home, list, edit, details, delete, tags, with_tag

urlpatterns = patterns('profile.views',
	(r'^$', 'list'),
	(r'^create.*$', 'edit'),
	(r'^edit/(?P<flow_id>\d+)/$', 'edit'),
	(r'^(?P<slug>[-\w]+)$', 'details'),
	(r'^delete/(?P<flow_id>\d+)/$', 'delete'),
)
