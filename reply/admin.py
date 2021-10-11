from django.contrib import admin
from .models import Reply
from mptt.admin import DraggableMPTTAdmin
# Register your models here.



admin.site.register(Reply, DraggableMPTTAdmin)