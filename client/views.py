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

from models import Work
from tagging.models import Tag, TaggedItem

import django.shortcuts as shortcuts
import django.http as http
import models


# Create your views here.
def home(request):
	worklist = Work.objects.all()
	return render_to_response('index.html', {'worklist':worklist,}, context_instance=RequestContext(request))

@login_required
def list(request):
    worklist = Work.objects.all()
    return render_to_response('client/job_list.html', {'worklist':worklist,}, context_instance=RequestContext(request))

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ['creation_date', 'slug']

@login_required
def edit(request, work_id = None):
	work = None
	if work_id is not None:
		work = get_object_or_404(Job, pk=work_id)

	if request.method == 'POST':
		form = JobForm(request.POST, instance=work)
		if form.is_valid():
			newwork = form.save(commit=False)
			newwork.user = request.user
			newwork.save()
			return HttpResponseRedirect(newwork.get_absolute_url())
	else:
		form = JobForm(instance=work)
	return render_to_response('client//job_edit.html', {'form':form, 'work':work,}, context_instance=RequestContext(request))

connection._rollback()

def details(request, slug):
	work = get_object_or_404(Job, slug=slug)
	return render_to_response('client/job_detail.html', {'work':work,}, context_instance=RequestContext(request))

@login_required
def delete(request, work_id):
	work = Work.objects.get(pk=work_id)
	work.delete()
	return HttpResponseRedirect('/get-work/')

def tags(request):
		return render_to_response('tag/tag_archive.html', {}, context_instance=RequestContext(request))

def with_tag(request, tag, object_id=None, page=1):
	query_tag = Tag.objects.get(name=tag)
	entries = TaggedItem.objects.get_by_model(models.Job, query_tag)

	return render_to_response('tag/tag_list.html', {"tag":tag, "entries":entries}, context_instance=RequestContext(request))
