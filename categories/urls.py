from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from categories.models import Category

urlpatterns = patterns('',
    url(r'^list/$', ListView.as_view(model = Category), name='categories_list'),

    )
