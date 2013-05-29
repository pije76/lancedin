from django.db import models, connection
from django.db.models import CharField, DateField, ForeignKey, Model, permalink, signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _, ugettext as _
from django.db.models.signals import post_save
from django.utils.encoding import smart_unicode

from tagging.fields import TagField
from tagging.models import Tag
from ratings.handlers import ratings
from ratings.forms import SliderVoteForm
from userena.models import UserenaBaseProfile
from haystack import indexes
from haystack.sites import site
from datetime import datetime

import datetime
import tagging

# Create your models here.
class Profile(UserenaBaseProfile):

	user =  models.OneToOneField(User, unique=True, verbose_name =('user'), related_name = '+')
	first_name = models.CharField("First Name", max_length=80)
	last_name = models.CharField("Last Name", max_length=80)
	email = models.URLField("URL")
	city = models.CharField("City", max_length=80)
	country = models.CharField("Country", max_length=80)
	title = models.CharField("Title", max_length=80)
	rate = models.CharField("Hourly Rate", max_length=80)
	#skill = TagField("Skill", blank=False, help_text='comma separated')
	education = models.CharField("Education", max_length=80)
	employment = models.CharField("Employment History", max_length=80)
	portfolio = models.CharField("Portfolio", max_length=80)
	certificate = models.CharField("Certifications", max_length=80)

	class Meta:
		verbose_name = 'Freelancer'

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
