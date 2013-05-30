from django.db import models
from django.db.models import permalink, signals
from django.db.models.signals import post_save
from django.utils.html import escape  #use for friendly name in the email
from django.utils.safestring import mark_safe #use for friendly name in the email

#from tagging.fields import TagField
#from tagging.models import Tag
#from categories.models import Category

TYPE_CHOICES = (
    ('HR', 'Hourly'),
    ('FX', 'Fixed Price'),
)

RATE_CHOICES = (
    ('5', '$0-$5 /hour'),
    ('10', '$5-$10 /hour'),
    ('20', '$10-$20 /hour'),
    ('30', '$20-$30 /hour'),
    ('40', '$30-$40 /hour'),
    ('50', '$40-$50 /hour'),
    ('60', '$50-$60 /hour'),
    ('70', '$60-$70 /hour'),
    ('80', '$70-$80 /hour'),
    ('90', '$80-$90 /hour'),
    ('100', '$90-$100 /hour'),
)

BUDGET_CHOICES = (
    ('50', '< $50'),
    ('100', '$50-$100'),
    ('500', '$100-$500'),
    ('1000', '$500-$1K'),
    ('5000', '$5K-$10K'),
    ('10000', '$10K >'),
)

WORKLOAD_CHOICES = (
    ('needed', 'As needed'),
    ('part_time', 'Part Time'),
    ('full_time', 'Full Time'),
)

DURATION_CHOICES = (
    ('1_week ', 'Less than 1 week'),
    ('1_month ', 'Less than 1 month'),
    ('3_month', '1 month - 3 month'),
    ('6_month', '3 month - 6 month'),
    ('6+_month', 'More than 6 month'),
)

# Create your models here.
class Job (models.Model):
	title = models.CharField("Job Title", max_length=500)
	slug = models.SlugField(unique=True, help_text='Automatically built from the title')
	categories = models.ManyToManyField('category.Category', help_text='Categorize this item.')
	skill = models.ManyToManyField('category.Tag', help_text='Tag this item.')
	#skill = TagField("Skill", blank=False, help_text='comma separated')
	#category = models.ForeignKey('categories.Category')
	#category = models.ManyToManyField(Category)
	description = models.TextField("Job Description")
	type = models.CharField("Job Type", max_length=60, choices=TYPE_CHOICES,)
	rate = models.CharField("Rate", max_length=60, choices=RATE_CHOICES,)
	budget = models.CharField("Budget", max_length=60, choices=BUDGET_CHOICES,)
	workload = models.CharField("Workload", max_length=60, choices=WORKLOAD_CHOICES,)
	duration = models.CharField("Duration", max_length=60, choices=DURATION_CHOICES,)
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
		return ('client.views.details', (), {'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super(Job, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Job'
