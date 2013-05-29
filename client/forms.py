from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from models import Job
from tagging.forms import TagField
from captcha.fields import CaptchaField
from contact_form.forms import ContactForm
from userena.forms import SignupForm

class SignupFormExtra(SignupForm):
	avatar = forms.ImageField()
	first_name = forms.CharField(label=_(u'First name'), max_length=30, required=False)
	last_name = forms.CharField(label=_(u'Last name'), max_length=30, required=False)

	def __init__(self, *args, **kw):
		super(SignupFormExtra, self).__init__(*args, **kw)
		# Put the first and last name at the top
		new_order = self.fields.keyOrder[:-2]
		new_order.insert(0, 'first_name')
		new_order.insert(1, 'last_name')
		self.fields.keyOrder = new_order

	def save(self):
		new_user = super(SignupFormExtra, self).save()

		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.save()

		profile = new_user.get_profile()
		profile.mugshot = self.cleaned_data['avatar']
		profile.save()

		return new_user

class JobForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	url = forms.URLField()
	tags = TagField()
	flow_date = forms.DateTimeField()

	class Meta:
		model = Job
		exclude = ['author', 'creation_date']

class CaptchaContactForm(ContactForm):
	captcha = CaptchaField(help_text="(case insensitive)")
