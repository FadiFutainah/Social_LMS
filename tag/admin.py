from django.contrib import admin

# Register your models here.

from .models import *

models = (Tag, SuggestedTags, TaggedItem)

admin.site.register(models)