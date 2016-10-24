from __future__ import unicode_literals

from django.db import models

class Role(models.Model):
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    title = models.CharField(max_length=32)


class People(models.Model):
    class Meta:
        verbose_name_plural = "people"
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    github = models.CharField(max_length=40, blank=True)
    twitter = models.CharField(max_length=16, blank=True)
    web = models.URLField(max_length=255, blank=True)
    email = models.CharField(max_length=128, blank=True)
    position = models.CharField(max_length=32, blank=True)
    roles = models.ManyToManyField(Role)

    created = models.DateTimeField(auto_now_add=True) # update automatically on creation
    updated = models.DateTimeField(auto_now=True) # update automatically on save
