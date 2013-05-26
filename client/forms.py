from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from models import Work
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

class WorkForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	url = forms.URLField()
	tags = TagField()
	flow_date = forms.DateTimeField()

	class Meta:
		model = Work
		exclude = ['author', 'creation_date']

class CaptchaContactForm(ContactForm):
	captcha = CaptchaField(help_text="(case insensitive)")
