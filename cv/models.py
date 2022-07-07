from MySQLdb import Date
from django.db import models
from  django.contrib.auth.models import User

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    genders = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]
    
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=genders, max_length=1)
    points = models.PositiveBigIntegerField()
    age = models.PositiveIntegerField()
    photo = models.ImageField(null=True)
    address = models.CharField(max_length=255)
    services = models.TextField()
    bio = models.TextField()
    birth_date = models.DateField(null=True)
    is_graduated = models.BooleanField(default=False)
    start_date = models.DateField(null=True)    
    end_date = models.DateField(null=True)    
    
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_certified = models.BooleanField(default=False)
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    end_date = models.DateField(null=True)
    start_date = models.DateField()
    description = models.TextField()
    link = models.URLField(null=True)
    members = models.ManyToManyField(Profile, through='Membership', verbose_name='members')
    is_cerified = models.BooleanField(default=False)
    
class Membership(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    
class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    mark = models.PositiveIntegerField()
    data = models.DateField()