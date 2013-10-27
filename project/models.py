from django.db import models
from django.db.models import permalink, signals
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google
from django.core.exceptions import *

from tagging.fields import TagField
from haystack import indexes
from mptt.models import MPTTModel, TreeForeignKey

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
    slug = models.SlugField(max_length=200, unique=True, help_text='Automatically built from the title.')
    category = models.ForeignKey('project.Category', null=True)
#    sub_category = models.ForeignKey('project.SubCategory', null=True)
    skill = models.ManyToManyField('project.Skill')
    description = models.TextField("project Description")
    project_type = models.CharField("Project Type", max_length=60, choices=TYPE_CHOICES,)
    rate = models.CharField("Rate", max_length=60, choices=RATE_CHOICES,)
    budget = models.CharField("Budget", max_length=60, choices=BUDGET_CHOICES,)
    workload = models.CharField("Workload", max_length=60, choices=WORKLOAD_CHOICES,)
    duration = models.CharField("Duration", max_length=60, choices=DURATION_CHOICES,)
    create_date = models.DateTimeField('Date Published', auto_now_add=True, blank=True, null=True)
    expire_date = models.DateField('Expire Date', default=get_expire, blank=True, null=True, db_index=True)
    company = models.ForeignKey('company.Profile', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

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

    @models.permalink
    def get_absolute_url(self):
#        return ('project.views.project_detail', self.slug)
#        return ('project.views.project_detail', (), {'slug': self.slug})
        return ('project.views.project_detail', (), {'category': self.category.slug, 'slug': self.slug})
#        return u'/%s/%s/' % (self.category.slug, self.slug)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
#        self.description = markdown(self.description)
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Project, self).save(force_insert, force_update, *args, **kwargs)
        try:
            ping_google()
        except Exception:
        # Bare 'except' because we could get a variety
        # of HTTP-related exceptions.
            pass

    class Meta:
        ordering = ('-create_date',)
        get_latest_by = 'create_date'
        verbose_name = 'Project'


class Category(MPTTModel):
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    def __unicode__(self):
        if self.parent:
            return u'%s: %s' % (self.parent.title, self.title)
        return u'%s' % (self.title)

    def get_count(self):
        return Category.objects.filter(title=self).count()

    @permalink
    def get_absolute_url(self):
        return ('project.views.project_category', (), {'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('slug', 'parent',)
#        level_attr = 'mptt_level'
#        order_insertion_by = ['title']


#class SubCategory(models.Model):
#    title = models.CharField(max_length=200, unique=True, blank=False)
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

#tagging.register(Skill, tag_descriptor_attr='etags')
