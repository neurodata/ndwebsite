from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
    class Meta:
        verbose_name_plural = "people"
        
    name = models.CharField(max_length=64)
    github = models.CharField(max_length=40, blank=True)
    twitter = models.CharField(max_length=16, blank=True)
    web = models.URLField(max_length=255, blank=True)
    email = models.CharField(max_length=128, blank=True)

    created = models.DateTimeField(auto_now_add=True) # update automatically on creation
    updated = models.DateTimeField(auto_now=True) # update automatically on save

