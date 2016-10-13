from django.contrib import admin

from .models import People

# Register your models here.
class PeopleAdmin(admin.ModelAdmin):
    fields = ('name', 'github', 'twitter', 'web', 'email')
    list_display = ('name', 'github', 'twitter', 'web', 'email')

admin.site.register(People, PeopleAdmin)
