from django.db import models, connection
from django.db.models import CharField, DateField, ForeignKey, Model, permalink, signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
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
	website = models.URLField(_('website'), blank=True, verify_exists=True)

	class Meta:
		verbose_name = 'Profile'

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Freelancer (models.Model):
	title = models.CharField("Name", max_length=200)
	slug = models.SlugField(unique=True, help_text='Automatically built from the title')
	description = models.TextField("Description")
	url = models.URLField("URL")
	tags = TagField(blank=False, help_text='comma separated')
	creation_date = models.DateTimeField('Date published', auto_now_add=True, blank=True, null=True)
	user = models.ForeignKey('auth.User', null=True)

	def __unicode__(self):
		return self.title

	def add_to_search_index(sender, instance=None, **kwargs):
		try:
			index = site.get_index(instance.__class__)
		except:
			return

		index.backend.update(index, [instance])
	signals.post_save.connect(add_to_search_index)

	def delete_from_search_index(sender, instance=None, **kwargs):
		try:
			index = site.get_index(instance.__class__)
		except:
			return

		index.backend.remove(instance)
	signals.post_delete.connect(delete_from_search_index)

	def set_tags(self, tags):
		Tag.objects.update_tags(self, tags)

	def get_tags(self):
		return Tag.objects.get_for_object(self)

	@permalink
	def get_absolute_url(self):
		return ('freelancer.views.details', (), {'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super(Freelancer, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Freelancer'

tagging.register(Freelancer, tag_descriptor_attr='etags')
ratings.register(Freelancer, score_range=(1, 10), form_class=SliderVoteForm)
