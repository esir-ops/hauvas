from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Professor)
admin.site.register(models.Course)
admin.site.register(models.ModuleList)
admin.site.register(models.ModuleItem)
