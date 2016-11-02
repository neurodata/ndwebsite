from django.contrib import admin

from .models import FeaturedData, FeaturedTool

class FeaturedDataAdmin(admin.ModelAdmin):
    fields = ('priority', 'dataProject')
    list_display = fields

class FeaturedToolAdmin(admin.ModelAdmin):
    fields = ('priority', 'tool')
    list_display = fields

admin.site.register(FeaturedData, FeaturedDataAdmin)
admin.site.register(FeaturedTool, FeaturedToolAdmin)
