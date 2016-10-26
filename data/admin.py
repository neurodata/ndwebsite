from django.contrib import admin

from .models import DataProject, DataType, ExploreTile

# Register your models here.
class DataProjectAdmin(admin.ModelAdmin):
    fields = ('token', 'title', 'background_image', 'desc', 'license')
    list_display = ('title', 'token', 'created', 'updated')

class DataTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(DataProject, DataProjectAdmin)
admin.site.register(DataType, DataTypeAdmin)
