from django.shortcuts import render

def home(request):
  context = {}
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def uikit(request):
  return render(request, 'ui-kit.html')
