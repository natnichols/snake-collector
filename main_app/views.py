# imports
from django.shortcuts import render

# views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def snake_index(request):
  return render(request, 'snakes/index.html', { 'snakes': snakes })