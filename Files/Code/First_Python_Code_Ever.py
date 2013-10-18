# This is the very first lines of code ever written at Sprint.ly. Just 
# some stubbed Django modles that were uploaded to Basecamp on
# March 21, 2010.

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    created_at = models.DateTimeField()
    developers = models.ManyToManyField(User) # Need to split into a model through

    def __unicode__(self):
        return self.title

class Sprint(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_at = models.DateTimeField()
    
class Feature(models.Model):
    sprint = models.ForeignKey(Sprint)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    
class Task(models.Model):
    feature = models.ForeignKey(Feature)
    title = models.CharField(max_length=100)
    description = models.TextField()
    hours_estimate = models.IntegerField()
