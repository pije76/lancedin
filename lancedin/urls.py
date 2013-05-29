from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template, redirect_to

from haystack.views import SearchView
from tagging.views import tagged_object_list

from client.models import Job
from client.views import home, list, edit, details, delete, tags, with_tag
#from client.forms import CaptchaContactForm as ContactForm, SignupFormExtra

from profile.models import Profile
from profile.views import home, list, edit, details, delete, tags, with_tag
#from profile.forms import CaptchaContactForm as ContactForm, SignupFormExtra

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {
    'queryset': Job.objects.filter(),
    'date_field': 'creation_date',
}

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'client.views.home', name='home'),
    #url(r'^$', include('pin.urls')),
    # url(r'^lancedin/', include('lancedin.foo.urls')),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'index.html'}, 'index' ),

    # Uncomment the admin/doc line below to enrib.admindocs.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),

    (r'^get-work/', include('client.urls')),
    (r'^hire-freelancer/', include('profile.urls')),
#    (r'^how-it-works/', include('freelancer.urls')),
#   url(r'^myjob/$', direct_to_template, {'template': 'client/my_job.html'}, name='myjoblist'),

    (r'^tags/$', 'client.views.tags'),
    (r'^tag/([-_A-Za-z0-9]+)/$','client.views.with_tag'),

    (r'^search/', include('haystack.urls')),
#    (r'^tinymce/', include('tinymce.urls')),

    (r'^profile/', include('userena.urls')),
#    (r'^freelancer/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
#    (r'^client/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
    #(r'^accounts/', include('registration.backends.default.urls')),

    #url(r'^captcha/', include('captcha.urls')),
    #(r'^contact/', include('contact_form.urls'), {'form_class': ContactForm}),
)
