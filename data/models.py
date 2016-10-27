from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DataType(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, blank=False)

class DataProject(models.Model):
    token = models.CharField(max_length=255, primary_key=True)

    title = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    license = models.TextField(blank=True)

    list_image_src = models.CharField(max_length=128, default="/assets/img/tools/placeholder.png")
    background_image = models.CharField(max_length=128, default='assets/img/tools/default_header.jpg')


    created = models.DateTimeField(auto_now_add=True) # update automatically on creation
    updated = models.DateTimeField(auto_now=True) # update automatically on save

    types = models.ManyToManyField(DataType)

class ExploreTileType(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, blank=False)

class ExploreTile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    modality = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    cuboids = models.CharField(max_length=255, blank=True)
    cuboid_size = models.CharField(max_length=255, blank=True)
    voxels = models.CharField(max_length=255, blank=True)

    dataproject = models.ForeignKey('DataProject', null=True)

    image = models.CharField(max_length=128, default="/assets/img/tools/placeholder.png")

    types = models.ManyToManyField(ExploreTileType)

    def __unicode__(self):
        return self.name

class TileType(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, blank=False)

class Tile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)

    desc = models.TextField(blank=True)

    dataproject = models.ForeignKey('DataProject', null=True)

    image = models.CharField(max_length=128, default="/assets/img/tools/placeholder.png")

    types = models.ManyToManyField(TileType)
