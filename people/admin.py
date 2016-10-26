from django.contrib import admin

from .models import People
from .models import Role

# Register your models here.
class PeopleAdmin(admin.ModelAdmin):
    fields = ('name', 'github', 'twitter', 'web', 'email', 'position', 'image_src', 'roles')
    list_display = ('name', 'github', 'twitter', 'web', 'email', 'position', 'image_src')
    filter_horizontal = ('roles',)

class RoleAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)

admin.site.register(People, PeopleAdmin)
admin.site.register(Role, RoleAdmin)
