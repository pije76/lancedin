from django import forms
from django.forms import ModelForm

from models import Project, Category, SubCategory, Skill
from tagging.forms import TagField
from userena.forms import SignupForm


class ProjectForm(forms.Form):
    title = forms.CharField(required=True)
    slug = forms.SlugField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")
    skill = TagField()
    description = forms.CharField(required=True)
    creation_date = forms.DateTimeField()

    class Meta:
        model = Project
        exclude = ['creation_date']
        fields = ('title', 'category', 'project_type', 'description', 'company', 'location')
