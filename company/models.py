from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us import models as us_models

from userena.models import UserenaBaseProfile
#from country_utils.fields import CountryField


# Create your models here.
class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name = '+')
    name = models.CharField("Company Name", max_length=80)
    address = models.TextField(blank=True, null=True)
    logo = models.CharField("Company Logo", max_length=80)
    website = models.URLField("Company Website", max_length=80, verify_exists=False, null=True, blank=True, help_text=_('"www.company.com"'))
    email = models.EmailField("Email", max_length=254)
#    country = CountryField(blank=False)
#    location = models.ForeignKey('company.Location', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


#class Location(models.Model):
#    city = models.CharField(max_length=64)
#    state = us_models.USStateField()

#    def __unicode__(self):
#        return "%s, %s" % (self.city, self.state)
