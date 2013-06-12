from django.contrib.auth.models import User

from project.models import Project

from haystack.indexes import *
from haystack import site, indexes

import datetime
import pdb


class ProjectIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description', faceted=True)
    duration = indexes.CharField(model_attr='duration', faceted=True)

    def index_queryset(self):
        return Project.objects.filter(create_date__lte=datetime.datetime.now())

    def update_object(self, instance, **kwargs):
        pdb.set_trace()
        return super(ProjectIndex, self).update_object(instance, **kwargs)

site.register(Project, ProjectIndex)
