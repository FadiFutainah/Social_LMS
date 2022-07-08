from weakref import ReferenceType
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    background = models.ImageField()
    icon = models.ImageField()
    view_template = models.TextField(null=True)
    importance_and_advantages = models.TextField()
    advice_and_tools = models.TextField()
    
    students = models.ManyToManyField(User, through='StudentPage')
    dependencies = models.ManyToManyField('Page', through='PageDependency', related_name='dependency_set')
    references = models.ManyToManyField('Page', through='PageReference', related_name='reference_set')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'page'

class PageDependency(models.Model):
    parent_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='parent_dependencies')
    dependant_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='dependant_pages', null=True)
    
    class Meta:
        db_table = 'page_depenency'


class PageReference(models.Model):
    parent_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='parent_references')
    referenced_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='referenced_pages')
    # TODO: explain the link
    link = models.CharField(max_length=255)
    index = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'page_reference'


class Feedback(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content = models.TextField()

class StudentPage(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) 
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'student_page'

class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Feature(models.Model):
    page_reference = models.ForeignKey(PageReference, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=255, default=0)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    