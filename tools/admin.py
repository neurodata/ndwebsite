from django.contrib import admin

from .models import Tool, ToolType

class ToolAdmin(admin.ModelAdmin):
    fields = ('token', 'longname', 'short_description', 'long_description',
        'list_image_src', 'header_image_src', 'api_url', 'code_url',
        'docs_url', 'press_url', 'contributers_url',
        'types')
    list_display = ('token', 'longname')
    filter_horizontal = ('types',)

class ToolTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(Tool, ToolAdmin)
admin.site.register(ToolType, ToolTypeAdmin)
