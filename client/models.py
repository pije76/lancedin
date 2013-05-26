from django.db import models
from django.db.models import permalink, signals
from django.db.models.signals import post_save

from tagging.fields import TagField
from tagging.models import Tag
from categories.models import Category

# Create your models here.
class Work (models.Model):
	title = models.CharField("Job Title", max_length=200)
	#category = models.ForeignKey('categories.Category')
	category = models.ManyToManyField(Category)
	description = models.TextField("Job Description")
	skill = models.CharField("Skill", max_length=200)
	type = models.CharField("Type", max_length=60)
	slug = models.SlugField(unique=True, help_text='Automatically built from the title')
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
		return super(Work, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Work'
