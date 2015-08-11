from django.contrib import admin
from web_models import models
# Register your models here.
admin.site.register(models.Server)
admin.site.register(models.Cpu)
admin.site.register(models.Memory)
admin.site.register(models.Disk)