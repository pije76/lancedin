# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_delete
from django.db import connection, transaction
from django.views.generic import ListView, DetailView
from django.views.generic.list_detail import object_detail, object_list
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.template import RequestContext

from models import Profile
from tagging.models import Tag, TaggedItem

import django.shortcuts as shortcuts
import django.http as http
import models


# Create your views here.
def home(request):
	profilelist = Profile.objects.all()
	return render_to_response('index.html', {'profilelist':profilelist,}, context_instance=RequestContext(request))

@login_required
def list(request):
    profilelist = Profile.objects.all()
    return render_to_response('profile/profile_list.html', {'profilelist':profilelist,}, context_instance=RequestContext(request))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['creation_date', 'slug']

@login_required
def edit(request, profile_id = None):
	profile = None
	if profile_id is not None:
		profile = get_object_or_404(Profile, pk=profile_id)

	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			newprofile = form.save(commit=False)
			newprofile.user = request.user
			newprofile.save()
			return HttpResponseRedirect(newprofile.get_absolute_url())
	else:
		form = ProfileForm(instance=profile)
	return render_to_response('profile/profile_edit.html', {'form':form, 'profile':profile,}, context_instance=RequestContext(request))

connection._rollback()

def details(request, slug):
	profile = get_object_or_404(Profile, slug=slug)
	return render_to_response('profile/profile_detail.html', {'profile':profile,}, context_instance=RequestContext(request))

@login_required
def delete(request, profile_id):
	profile = Profile.objects.get(pk=profile_id)
	profile.delete()
	return HttpResponseRedirect('/get-profile/')

def tags(request):
		return render_to_response('tag/tag_archive.html', {}, context_instance=RequestContext(request))

def with_tag(request, tag, object_id=None, page=1):
	query_tag = Tag.objects.get(name=tag)
	entries = TaggedItem.objects.get_by_model(models.Profile, query_tag)

	return render_to_response('tag/tag_list.html', {"tag":tag, "entries":entries}, context_instance=RequestContext(request))
