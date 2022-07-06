from django.db import models
from  django.contrib.auth.models import User

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    genders = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]
    
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=genders, max_length=1)
    points = models.PositiveBigIntegerField()
    study_year = models.CharField(max_length=4)
    age = models.PositiveIntegerField()
    photo = models.ImageField(null=True)
    address = models.CharField(max_length=255)
    services = models.TextField()
    bio = models.TextField()
    
class Experience(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=55)
    
class Contact(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    end_date = models.DateField()
    start_date = models.DateField()
    description = models.TextField()
    projects = models.ManyToManyField(Profile, through='Membership')
    
class Membership(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)