from django.shortcuts import render 

def home(request):
  context = {} 
  return render(request, 'index.html', context)

def uikit(request):
  return render(request, 'ui-kit.html')


