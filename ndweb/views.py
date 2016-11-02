import random

from django.shortcuts import render

from .models import FeaturedData, FeaturedTool
from people.models import People, Role

def home(request):
    personCount = People.objects.count()
    randomPerson = None
    if personCount > 0:
        randomPerson = People.objects.all()[random.randint(0, personCount - 1)]
    featuredTools = FeaturedTool.objects.all()
    featuredData = FeaturedData.objects.all()

    context = {
        'randomPerson' : randomPerson,
        'featuredTools' : featuredTools,
        'data_projects' : featuredData,
    }
    return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def uikit(request):
  return render(request, 'ui-kit.html')
