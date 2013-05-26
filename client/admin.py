from django.contrib import admin

from models import Work

from categories.forms import CategoriesFormMixin

class CategorizedWorkForm(CategoriesFormMixin):
	pass

class CategorizedPhotoSetAdmin(admin.ModelAdmin):
	form = CategorizedWorkForm

admin.site.register(Work, CategorizedPhotoSetAdmin)
