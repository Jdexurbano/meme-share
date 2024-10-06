from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_link')

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
