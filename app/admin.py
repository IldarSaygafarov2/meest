from django.contrib import admin
from .models import UserRequest

# Register your models here.


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'track_number', 'fullname', 'passport_series', 'passport_number', 'pinfl', 'phone_number')
    list_display_links = ('pk', 'track_number')


admin.site.register(UserRequest, UserRequestAdmin)