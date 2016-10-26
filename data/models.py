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

    background_image = models.ImageField(upload_to='templates/static/upload/data/', blank=True)

    created = models.DateTimeField(auto_now_add=True) # update automatically on creation
    updated = models.DateTimeField(auto_now=True) # update automatically on save

    types = models.ManyToManyField(DataType)

class ExploreTile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    modality = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    cuboids = models.CharField(max_length=255, blank=True)
    cuboid_size = models.CharField(max_length=255, blank=True)
    voxels = models.CharField(max_length=255, blank=True)

    dataproject = models.ForeignKey('DataProject', null=True)

    image = models.ImageField(upload_to='upload/tile/explore/')

    SUBCATEGORY_CHOICES = (
        ('Images', 'Images'),
        ('Time', 'Time'),
        ('Matrices', 'Matrices'),
        ('Shapes', 'Shapes'),
        ('Graphs', 'Graphs')
    )
    subcategory = models.CharField(max_length=255, choices=SUBCATEGORY_CHOICES)
