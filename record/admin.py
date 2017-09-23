from django.contrib import admin

from .models import UserAction

# Register your models here.


class UserActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created', 'ip_address' )

admin.site.register(UserAction, UserActionAdmin)