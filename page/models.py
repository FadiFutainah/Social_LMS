from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    background = models.ImageField()
    icon = models.ImageField()
    importance = models.TextField()
    advantages = models.TextField()
    students = models.ManyToManyField(User, through='StudentPage')
    dependencies = models.ManyToManyField('Page', through='PageDependency')
    tools = models.ManyToManyField('Tool', db_table='page_tools')

    class Meta:
        db_table = 'page'

class PageDependency(models.Model):
    parent_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='parent_pages')
    referenced_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='referenced_pages')
    feature = models.ForeignKey('Feature', on_delete=models.SET_NULL, null=True)
    feature_value = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'page_depenency'

class StudentPage(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) 
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    feedback = models.TextField()
    advice = models.TextField()
    
    class Meta:
        db_table = 'student_page'

class Feature(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
class Link(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    value = models.CharField(max_length=1024)
    
class Tool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()