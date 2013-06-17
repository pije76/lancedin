from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from models import Project, Category, Skill
from tagging.forms import TagField


class ProjectForm(forms.Form):
    title = forms.CharField(required=True)
    slug = forms.SlugField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")
    skill = TagField()
    description = forms.CharField(required=True)
    create_date = forms.DateTimeField()

    class Meta:
        model = Project
        exclude = ['create_date']
        fields = ('title', 'category', 'description')
