from django.contrib import admin

from models import Job, Category, Skill


class JobAdmin (admin.ModelAdmin):
    list_display = ('title', 'category', 'company', 'create_date')
    search_fields = ('title', 'description')
    list_filter = ('company', 'create_date')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}

# Register your own admin class and attach it to the model
admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill)
