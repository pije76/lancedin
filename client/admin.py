from django.contrib import admin

from models import Job

#from categories.forms import CategoriesFormMixin

#class CategorizedJobForm(CategoriesFormMixin):
#	pass

#class CategorizedPhotoSetAdmin(admin.ModelAdmin):
#	form = CategorizedWorkForm

#admin.site.register(Client)
admin.site.register(Job)
#admin.site.register(Job, CategorizedPhotoSetAdmin)
