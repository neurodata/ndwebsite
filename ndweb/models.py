from __future__ import unicode_literals

from django.db import models
from data.models import DataProject
from tools.models import Tool

class FeaturedData(models.Model):
    class Meta:
        ordering = ('priority',)
        verbose_name_plural = "Featured data"

    priority = models.IntegerField(default=0)
    dataProject = models.OneToOneField(DataProject, null=False)

class FeaturedTool(models.Model):
    class Meta:
        ordering = ('priority',)

    priority = models.IntegerField(default=0)
    tool = models.OneToOneField(Tool, null=False)
