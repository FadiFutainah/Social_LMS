from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_up = models.BooleanField()
    
    class Meta:
        db_table = 'rate'
        
        
class RatedItem(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, db_column='item')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    class Meta:
        db_table = 'rated_item'