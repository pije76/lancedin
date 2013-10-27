import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Django settings for lancedin project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'lancedin.db',                      # Or path to database file if using sqlite3.
        'USER': 'pije76',                      # Not used with sqlite3.
        'PASSWORD': 'tratap60',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xg*2t5k#@v83+klpytzyks^vbf_xnwsu_$6=7r=6$w^ur4o@46'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'watson.middleware.SearchContextMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'seo_cascade.middleware.SEOMiddleware',
)

ROOT_URLCONF = 'lancedin.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'lancedin.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.csrf",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    #"pybb.context_processors.processor",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    #'django.contrib.comments',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    #'django.contrib.gis',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'company',
    'freelancer',
    'profile',
    'project',

    #'classifieds',
    #'taxonomy',
    #'category',
    #'categories',
    #'categories.editor',
    'mptt',
    #'mpttmenu',
    #'django_mptt_admin',
    #'commons',
    #'wmd',
    #'pin', #pinterest
    #'daddy_avatar', #pinterest
    #'sorl.thumbnail', #pinterest

    #'ratings',
    #'reputation',
    #'captcha',
    #'contact_form',
    #'tinymce',
    #'isotope', #pinterest
    #'jquery',
    #'html5accordion',
    #'masonry', #pinterest
    #'endless_pagination', #pinterest
    #'suit',

    #'country_utils',
    #'cities',
    #'cities_light',
    #'countries',

    #'pybb',

    #'bootstrapform',
    #'userenabootstrap',
    'userena',
    'guardian',
    #'registration',
    #'profile',

    'haystack',
    #'celery_haystack',
    'watson',
    'south',
    'debug_toolbar',
    'compressor',  # pinterest

    'tagging',
    #'tagging_autocomplete_tagit',
    #'editable',
    #'taggit', #pinterest
    #'compressor',
    #'paypal.standard.ipn',
    #'tastypie',
    #'seo',
    #'rollyourown.seo',
    #'meta',
    #'robots',
    #'static_sitemaps',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Userena configuration #
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'panjul76@gmail.com'
#EMAIL_HOST_PASSWORD = 'tratap60'

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = "profile.Profile"

USERENA_ACTIVATION_REQUIRED = False
USERENA_SIGNIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/profile/%(username)s/'
LOGIN_URL = '/profile/signin/'
LOGOUT_URL = '/profile/signout/'

# PYBB configuration #
#PYBB_SMILES = {
#    '&gt;_&lt;': 'angry.png',
#    ':.(': 'cry.png',
#    'o_O': 'eyes.png',
#    '[]_[]': 'geek.png',
#    '8)': 'glasses.png',
#    ':D': 'lol.png',
#    ':(': 'sad.png',
#    ':O': 'shok.png',
#    '-_-': 'shy.png',
#    ':)': 'smile.png',
#    ':P': 'tongue.png',
#    ';)': 'wink.png'
#}

# Captcha configuration #
# http://code.google.com/p/django-simple-captcha/
#RECAPTCHA_PUBLIC_KEY = '6Ld51tsSAAAAAJhhowv56fiImWD1rop38IGavnpT '
#RECAPTCHA_PRIVATE_KEY = '6Ld51tsSAAAAAI75ZSipL10yqx21brhy_BeKCmXT '

# Haystack + Whoosh configuration #
#HAYSTACK_SITECONF = 'lancedin.search_sites'
#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'index.whoosh')
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#    },
#}

#HAYSTACK + Whoosh configuration
#HAYSTACK_SITECONF = 'lancedin.search_sites'
#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'index.whoosh')
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#    },
#}

# Haystack + SOLR configuration #
#HAYSTACK_SITECONF = 'lancedin.search_sites'
#HAYSTACK_SEARCH_ENGINE = 'solr'
#HAYSTACK_SEARCH_ENGINE = 'dummy' # Test For Ajax AutoComplete
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8080/solr'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8080/solr',
#        'TIMEOUT': 60 * 5,
#        'INCLUDE_SPELLING': True,
#        'BATCH_SIZE': 100,
    },
}

# Haystack + SOLR configuration for Heroku #
#HAYSTACK_URL = os.environ.get('WEBSOLR_URL', '')
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': HAYSTACK_URL,
#    },
#}

# Debug Toolbar configuration #
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}

# Django-Tagging Configuration #
FORCE_LOWERCASE_TAGS = True

# Django-Rating Configuration #
VALUATION_TEMPLATE = 'rating'

# South configuration #
SOUTH_TESTS_MIGRATE = False

# TinyMCE configuration #
TINYMCE_JS_URL = MEDIA_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_URL + 'js/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table,spellchecker,paste,searchreplace",
}
TINYMCE_SPELLCHECKER = True

REPUTATION_MAX_LOSS_PER_DAY = 200
REPUTATION_MAX_GAIN_PER_DAY = 200
REPUTATION_PERMISSONS = {'voting.can_vote_up': 50,
                         'voting.can_vote_down': 150}

# Django-Cities Configuration #
#CITIES_FILES = {
#    'city': {
#       'filename': 'cities1000.zip',
#       'urls':     ['http://download.geonames.org/export/dump/'+'{filename}']
#    },
#}
#CITIES_LOCALES = ['en', 'LANGUAGES']
#CITIES_POSTAL_CODES = ['US']
#CITIES_PLUGINS = [
#    'cities.plugin.postal_code_ca.Plugin',  # Canada postal codes need region codes remapped to match geonames
#]

# Django-Categories Configuration #
#CATEGORIES_SETTINGS = {
#    'M2M_REGISTRY': {
#        'freelancer.Profile': 'category',
#        'company.Project': (
#            {'name': 'category', 'related_name': 'category'},
#        ),
#    }
#}

# Django-MPTT Configuration
# default is 10 pixels
#MPTT_ADMIN_LEVEL_INDENT = 20

APPEND_SLASH = True

READ_MORE_TEXT = 'Read more...'

SEO_FOR_MODELS = [
    'project.models.Project',
    'project.models.Category',
]

META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = '127.0.0.1:8000'

ROBOTS_USE_SITEMAP = False
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24
#ROBOTS_SITEMAP_URLS = [
#    http://www.example.com/sitemap.xml,
#]

#STATICSITEMAPS_ROOT_SITEMAP = 'lancedin.sitemaps.sitemaps'

CATEGORIES_SETTINGS = {
    'FK_REGISTRY': {
        'project.Project': 'category',
    }
}
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Heroku configuration #
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

#POSTGRES_URL = "HEROKU_POSTGRESQL_<COLOR>_URL"
#DATABASES = {
#    'default': dj_database_url.config(default=os.environ[POSTGRES_URL])
#}

#DATABASES = {
#    'default': dj_database_url.config(default='postgres://cnzjpbuzbpqcyc:opCQfs3M6ZCjnCJE7zLF7iuUov@ec2-23-21-130-189.compute-1.amazonaws.com:5432/d9qoc9bsgsnqkg')
#}
