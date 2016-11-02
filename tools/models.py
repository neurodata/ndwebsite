from __future__ import unicode_literals

from django.db import models

class ToolType(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, blank=False)

class Tool(models.Model):
    def __str__(self):
        return self.token

    token = models.CharField(max_length=64, primary_key=True)
    longname = models.CharField(max_length=128)

    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)

    list_image_src = models.CharField(max_length=128, default="/assets/img/tools/placeholder.png")
    header_image_src = models.CharField(max_length=128, default="/assets/img/tools/default_header.jpg")

    api_url = models.URLField(max_length=255, blank=True)
    code_url = models.URLField(max_length=255, blank=True)
    issues_url = models.URLField(max_length=255, blank=True)
    docs_url = models.URLField(max_length=255, blank=True)
    press_url = models.URLField(max_length=255, blank=True)
    contributers_url = models.URLField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True) # update automatically on creation
    updated = models.DateTimeField(auto_now=True) # update automatically on save

    types = models.ManyToManyField(ToolType)
