import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_question = models.BooleanField(default=True)
    is_closed = models.BooleanField(default=False)
    closed_reply = models.ForeignKey('Reply', on_delete=models.SET_NULL, null=True, related_name='closed_reply')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    

    class Meta:
        db_table = 'forum'
        ordering = ['title']
        

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{self.user} on {self.forum.title}'
    