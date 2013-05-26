
from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from categories.models import Category

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'breadcrumb')
    prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20

    def queryset(self, request):
        """Limit the list of categories according to user"""
        return self.model._default_manager.choices(request.user)

admin.site.register(Category, CategoryAdmin)
