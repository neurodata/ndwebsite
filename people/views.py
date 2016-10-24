from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import People, Role

def peopleHome(request):
    # Do select * query
    people = People.objects.all().prefetch_related('roles');
    roles = Role.objects.all();

    return render(request, 'people.html', {
        'people_list' : people,
        'role_list' : roles
        })
