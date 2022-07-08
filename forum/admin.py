from django.contrib import admin

# Register your models here.

from .models import *

models = (Forum, Reply)

admin.site.register(models)