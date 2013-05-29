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

from models import Job
from tagging.models import Tag, TaggedItem

import django.shortcuts as shortcuts
import django.http as http
import models


# Create your views here.
def home(request):
	joblist = Job.objects.all()
	return render_to_response('index.html', {'joblist':joblist,}, context_instance=RequestContext(request))

@login_required
def list(request):
    joblist = Job.objects.all()
    return render_to_response('client/job_list.html', {'joblist':joblist,}, context_instance=RequestContext(request))

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['creation_date', 'slug']

@login_required
def edit(request, job_id = None):
	job = None
	if job_id is not None:
		job = get_object_or_404(Job, pk=job_id)

	if request.method == 'POST':
		form = JobForm(request.POST, instance=job)
		if form.is_valid():
			newjob = form.save(commit=False)
			newjob.user = request.user
			newjob.save()
			return HttpResponseRedirect(newjob.get_absolute_url())
	else:
		form = JobForm(instance=job)
	return render_to_response('client//job_edit.html', {'form':form, 'job':job,}, context_instance=RequestContext(request))

connection._rollback()

def details(request, slug):
	job = get_object_or_404(Job, slug=slug)
	return render_to_response('client/job_detail.html', {'job':job,}, context_instance=RequestContext(request))

@login_required
def delete(request, job_id):
	job = Job.objects.get(pk=job_id)
	job.delete()
	return HttpResponseRedirect('/get-job/')

def tags(request):
		return render_to_response('tag/tag_archive.html', {}, context_instance=RequestContext(request))

def with_tag(request, tag, object_id=None, page=1):
	query_tag = Tag.objects.get(name=tag)
	entries = TaggedItem.objects.get_by_model(models.Job, query_tag)

	return render_to_response('tag/tag_list.html', {"tag":tag, "entries":entries}, context_instance=RequestContext(request))
