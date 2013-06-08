from django.views.generic import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from models import Job, Category


# Create your views here.
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def job_category(request):
    jobcategory = Category.objects.all()
    return render_to_response('job/job_category.html', locals(), context_instance=RequestContext(request))


def job_list(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Given a category slug, display all items in a category.
    joblist = Job.objects.filter(category=category)
    return render_to_response("job/job_list.html", locals(), context_instance=RequestContext(request))


def job_detail(request, slug, category):
    category = Category.objects.filter(slug=category)
    jobdetail = Job.objects.filter(slug=slug)
    return render_to_response('job/job_detail.html', locals(),  context_instance=RequestContext(request))
#    return object_list(request, queryset=Category.objects.all(), paginate_by=20, template_name='job/job_list.html', extra_context={'category': category})
