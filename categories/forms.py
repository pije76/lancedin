from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from categories.models import Category

CATEGORIES_DEFAULT_HELP = _("""Categories for this item.""")
CATEGORIES_HELP = getattr(settings, 'CATEGORIES_HELP', CATEGORIES_DEFAULT_HELP)


class CategoriesFormMixin(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(required = False, queryset = Category.objects.choices(), widget = forms.CheckboxSelectMultiple(), help_text = CATEGORIES_HELP)

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        user = kwargs.pop('user', None)
        super(CategoriesFormMixin, self).__init__(*args, **kwargs)
        if queryset:
            self.fields['categories'].queryset = queryset
        else:
            if user:
                self.fields['categories'].queryset = Category.objects.choices(user)
            elif kwargs.get('instance', None):
                self.fields['categories'].queryset = Category.objects.choices(kwargs.get('instance').author)
        if kwargs.get('instance', None):
            self.fields['categories'].initial = kwargs['instance'].categories.all().values_list('id', flat = True)

    def save(self, force_insert = False, force_update = False, commit = True):
        instance = super(CategoriesFormMixin, self).save(commit = False)

        old_m2m = self.save_m2m
        def save_m2m():
            if old_m2m:
                old_m2m()
            instance.categories.clear()
            for category in self.cleaned_data['categories']:
                instance.categories.add(category)

        if commit:
            instance.save()
            save_m2m()
        else:
            self.save_m2m = save_m2m
        return instance

