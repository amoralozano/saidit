from django.contrib import admin
from .models import SaidItUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(SaidItUser, UserAdmin)
