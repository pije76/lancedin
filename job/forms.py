from django import forms
from django.forms import ModelForm

from models import Job, Category, SubCategory, Skill
from tagging.forms import TagField
from userena.forms import SignupForm


class JobForm(forms.Form):
    title = forms.CharField(required=True)
    slug = forms.SlugField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")
    skill = TagField()
    description = forms.CharField(required=True)
    creation_date = forms.DateTimeField()

    class Meta:
        model = Job
        exclude = ['creation_date']
        fields = ('title', 'category', 'job_type', 'description', 'company', 'location')
