from django.contrib import admin

from .models import DataProject, ExploreTile

# Register your models here.
class DataProjectAdmin(admin.ModelAdmin):
    fields = ('token', 'title', 'desc', 'license')
    list_display = ('title', 'token', 'created', 'updated')

admin.site.register(DataProject, DataProjectAdmin)
