from django.contrib import admin

from .models import DataProject, ExploreTile

# Register your models here.
class DataProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'desc', 'info')

admin.site.register(DataProject, DataProjectAdmin)
