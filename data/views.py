from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import DataProject, ExploreTile, ExploreTileType, Tile, TileType

# Create your views here.

def dataHome(request):
    return HttpResponse('data!')

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
