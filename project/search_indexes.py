import datetime
from haystack import indexes

from models import Project


class ProjectIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    slug = indexes.CharField(model_attr='slug')
    skill = indexes.CharField(model_attr='skill')
    create_date = indexes.DateTimeField(model_attr='create_date')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Project.objects.filter(create_date__lte=datetime.datetime.now())
