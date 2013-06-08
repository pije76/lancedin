from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaBaseProfile
from country_utils.fields import CountryField

# Create your models here.
class Profile(UserenaBaseProfile):

    user =  models.OneToOneField(User, unique=True, verbose_name =('user'), related_name = '+')
    name = models.CharField("Company Name", max_length=80)
    logo = models.CharField("Company Logo", max_length=80)
    website = models.URLField("Company Website", max_length=80, verify_exists=False, null=True, blank=True, help_text=_('"www.company.com"'))
    email = models.EmailField("Email", max_length=254)
    country = CountryField(blank=False)

    class Meta:
        verbose_name = 'Client'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
