from django.db import models
from django.db.models import permalink, CharField, Model
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.core import urlresolvers
from django.core.urlresolvers import reverse
from django.core.exceptions import *
#from django.contrib.syndication.feeds import Feed
#from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag
from mptt.models import MPTTModel, TreeForeignKey
#from tagging_autocomplete_tagit.models import TagAutocompleteTagItField
from autoslug import AutoSlugField
from datetime import datetime, timedelta

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
    ('contract', 'Contract'),
    ('internship', 'Internship'),
)

DURATION_CHOICES = (
    ('1_week ', 'Less than 1 week'),
    ('1_month ', 'Less than 1 month'),
    ('3_month', '1 month - 3 month'),
    ('6_month', '3 month - 6 month'),
    ('1_year', '6 month - 1 year'),
    ('1+_year', 'More than 1 year'),
)


def get_expire():
    return datetime.today() + timedelta(days=30)


# Create your models here.
class Project (models.Model):
    title = models.CharField("Project Title", max_length=200, unique=True)
    slug = AutoSlugField(max_length=200, unique=True, help_text='Automatically built from the title.')
    category = models.ForeignKey('project.Category', related_name='categories')
#    sub_category = models.ForeignKey('project.SubCategory')
    skill = models.ManyToManyField('project.Skill')
    description = models.TextField("project Description")
    project_type = models.CharField("Project Type", max_length=60, choices=TYPE_CHOICES,)
    rate = models.CharField("Rate", max_length=60, choices=RATE_CHOICES,)
    budget = models.CharField("Budget", max_length=60, choices=BUDGET_CHOICES,)
    workload = models.CharField("Workload", max_length=60, choices=WORKLOAD_CHOICES,)
    duration = models.CharField("Duration", max_length=60, choices=DURATION_CHOICES,)
    create_date = models.DateTimeField('Date Published', auto_now_add=True, blank=True, null=True)
    expire_date = models.DateField('Expire Date', default=get_expire, blank=True, null=True, db_index=True)
    company = models.ForeignKey('profile.Profile', blank=True, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
#        return ('project.views.project_detail', self.slug)
#        return ('project.views.project_detail', (), {'slug': self.slug})
        return ('project.views.project_detail', (), {'category': self.category.slug, 'slug': self.slug})
#        return u'/%s/%s/' % (self.category.slug, self.slug)

    def save(self, *args, **kwargs):
#        self.description = markdown(self.description)
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-create_date',)
        get_latest_by = 'create_date'
        verbose_name = 'Project'


class Category(MPTTModel):
    title = models.CharField(max_length=200, unique=True)
#    slug = models.SlugField(max_length=200, unique=True)
    slug = AutoSlugField(max_length=200, help_text='Automatically built from the title.')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    def __unicode__(self):
        if self.parent:
            return u'%s: %s' % (self.parent.title, self.title)
        return u'%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return ('project.views.project_category', (), {'slug': self.slug})

    class MPTTMeta:
        verbose_name_plural = "Categories"
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

#class SubCategory(models.Model):
#    title = models.CharField(max_length=200, unique=True)
#    slug = models.SlugField(max_length=200, unique=True)
#    category = models.ForeignKey('project.Category')

#    def __unicode__(self):
#        return u'%s' % (self.title)

#    class Meta:
#        verbose_name_plural = "Sub Categories"


class Skill(models.Model):
#    title = TagAutocompleteTagItField(max_tags=10)
    title = TagField()

    def __unicode__(self):
        return self.title

    def set_tags(self, tags):
        Skill.objects.update_tags(self, title)

    def get_tags(self):
        return Skill.objects.get_for_object(self)
