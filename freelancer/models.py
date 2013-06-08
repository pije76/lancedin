from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from userena.models import UserenaBaseProfile
#from country_utils.fields import CountryField

# Create your models here.
class Profile(UserenaBaseProfile):

    user =  models.OneToOneField(User, unique=True, verbose_name =('user'), related_name = '+')
    title = models.CharField("Title", max_length=80)
    first_name = models.CharField("First Name", max_length=80)
    last_name = models.CharField("Last Name", max_length=80)
    email = models.EmailField("Email", max_length=254)
#    country = CountryField(blank=False)
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
