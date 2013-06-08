from django.contrib import admin
from models import Profile

# Register your own admin class and attach it to the model
admin.site.register(Profile)
# Unregister userena's
#admin.site.unregister(Profile)
