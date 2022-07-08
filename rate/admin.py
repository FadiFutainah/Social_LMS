from django.contrib import admin

# Register your models here.

from .models import *

models = (Rate, RatedItem)

admin.site.register(models)