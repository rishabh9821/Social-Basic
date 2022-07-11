from statistics import mode
from django.contrib import admin
from blogApp import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Comment)