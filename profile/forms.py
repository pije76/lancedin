from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from models import Profile
from tagging.forms import TagField
from captcha.fields import CaptchaField
from contact_form.forms import ContactForm
from userena.forms import SignupForm

class SignupFormExtra(SignupForm):
	avatar = forms.ImageField()

	def save(self):
		new_user = super(SignupFormExtra, self).save()

		profile = new_user.get_profile()
		profile.mugshot = self.cleaned_data['avatar']
		profile.save()

		return new_user

class ProfileForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	url = forms.URLField()
	tags = TagField()
	profile_date = forms.DateTimeField()

	class Meta:
		model = Profile
		exclude = ['author', 'creation_date']

class CaptchaContactForm(ContactForm):
	captcha = CaptchaField(help_text="(case insensitive)")
