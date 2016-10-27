from django.contrib import admin

from .models import DataProject, DataType, ExploreTile, ExploreTileType, Tile, TileType

# Register your models here.
class ExploreTileInline(admin.StackedInline):
    model = ExploreTile
    extra = 0
    filter_horizontal = ('types',)

class TileInline(admin.StackedInline):
    model = Tile
    extra = 0
    filter_horizontal = ('types',)

class TileTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

class DataProjectAdmin(admin.ModelAdmin):
    fields = ('token', 'title', 'list_image_src', 'background_image', 'desc', 'license', 'types')
    list_display = ('title', 'token', 'created', 'updated')

    filter_horizontal = ('types',)

    inlines = [ ExploreTileInline, TileInline ]

class DataTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

class ExploreTileTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

admin.site.register(DataProject, DataProjectAdmin)
admin.site.register(DataType, DataTypeAdmin)
admin.site.register(ExploreTileType, ExploreTileTypeAdmin)
admin.site.register(TileType, TileTypeAdmin)
