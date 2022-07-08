from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    number_of_uses = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tag'
    
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, db_column='item')
    object_id = models.PositiveIntegerField()
    contnet_object = GenericForeignKey()
    
    class Meta:
        db_table = 'tagged_item'
    
class SuggestedTags(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,  db_column='item')
    object_id = models.PositiveIntegerField()
    contnet_object = GenericForeignKey()
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tag.name
    
    class Meta:
        db_table = 'suggested_tags'
        
