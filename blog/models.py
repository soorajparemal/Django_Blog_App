from __future__ import unicode_literals
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField('Blog Published On ')
    tags = TaggableManager()

    def __str__(self):
        return self.title
