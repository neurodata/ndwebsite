from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import DataProject

# Create your views here.

def dataHome(request):
    return HttpResponse('data!')

def dataPage(request, token):
    dataproject = get_object_or_404(DataProject, token=token)

    context = {
        'token': dataproject.token,
        'title': dataproject.title,
        'desc': dataproject.desc,
        'license': dataproject.license,
        'background_image': dataproject.background_image,
    }
    return render(request, 'data_page.html', context)
    #return HttpResponse(dataproject.title)
