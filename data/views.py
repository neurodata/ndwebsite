from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import DataProject, DataType, ExploreTile, ExploreTileType, Tile, TileType

# Create your views here.

def dataHome(request):
    dataprojects = DataProject.objects.all().prefetch_related('types')
    dataproject_types = DataType.objects.all()
    context = {
        'data_projects' : dataprojects,
        'data_project_types' : dataproject_types
    }
    return render(request, 'data_home.html', context)

def dataPage(request, token):
    dataproject = get_object_or_404(DataProject, token=token)

    exploretiletypes = ExploreTileType.objects.all()
    try:
        exploretiles = ExploreTile.objects.get(dataproject = dataproject).prefetch_related('types')
    except ExploreTile.DoesNotExist:
        exploretiles = None

    try:
        tiles = Tile.objects.get(dataproject = dataproject).prefetch_related('types')
    except Tile.DoesNotExist:
        tiles = None

    context = {
        'data' : dataproject,
        'explore_tiles' : exploretiles,
        'explore_tiles_types' : exploretiletypes,
        'tiles' : tiles,
    }
    return render(request, 'data_page.html', context)
