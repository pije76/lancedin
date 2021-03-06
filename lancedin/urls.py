from django.conf.urls import patterns, include, url
from django.conf import settings

from project.models import Project

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
#   url(r'^lancedin/', include('lancedin.foo.urls')),
    url(r'^$', 'project.views.index', name='index'),
#    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, 'index'),
#    (r'', include('django.contrib.flatpages.urls')),


    # Uncomment the admin/doc line below to enrib.admindocs.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),

    (r'^find-project/', include('project.urls')),
#    (r'^find-freelancer/', include('freelancer.urls')),
#    (r'^how-it-works/', include('freelancer.urls')),
#   url(r'^myproject/$', direct_to_template, {'template': 'company/my_project.html'}, name='myprojectlist'),

#    (r'^tags/$', 'project.views.tags'),
#    (r'^tag/([-_A-Za-z0-9]+)/$','project.views.with_tag'),
#    (r'^tagging_autocomplete_tagit/', include('tagging_autocomplete_tagit.urls')),

    (r'^search/', include('haystack.urls')),
#    (r'^tinymce/', include('tinymce.urls')),

    (r'^profile/', include('userena.urls')),
#    (r'^freelancer/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
#    (r'^company/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
    #(r'^accounts/', include('registration.backends.default.urls')),

    #url(r'^captcha/', include('captcha.urls')),
    #(r'^contact/', include('contact_form.urls'), {'form_class': ContactForm}),
)
