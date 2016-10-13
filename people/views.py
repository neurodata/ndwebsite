from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import People

def peopleHome(request):
    # Do select * query
    people = People.objects.all().order_by('-name')

    return render(request, 'people.html', {'people_list' : people})
