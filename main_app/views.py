# imports
from django.shortcuts import render
from .models import Snake

# views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def snake_index(request):
  snakes = Snake.objects.all()
  return render(request, 'snakes/index.html', { 'snakes': snakes })
