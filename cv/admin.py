from django.contrib import admin

# Register your models here.

from .models import *

models = (Profile, Experience, Contact, Project, Membership, Mark)  

admin.site.register(models)