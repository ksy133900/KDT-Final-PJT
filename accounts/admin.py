from django.contrib import admin
from .models import User, Profile

# Register your models here.


# admin.site.register(User)
# admin.site.register(Profile)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']
    list_display_links = ['id', 'nickname']
