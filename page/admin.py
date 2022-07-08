from django.contrib import admin

# Register your models here.

from .models import *

models = (Page, PageDependency, PageReference, Feedback, StudentPage, Content, Feature)

admin.site.register(models)