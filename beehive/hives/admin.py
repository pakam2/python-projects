from django.contrib import admin
from .models import HiveUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(HiveUser)
class MyUserAdmin(UserAdmin):
     list_display = ('email', 'first_name', 'last_name')
