# imports
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Snake

# views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def snake_index(request):
  snakes = Snake.objects.all()
  return render(request, 'snakes/index.html', { 'snakes': snakes })

def snake_detail(request, snake_id):
  snake = Snake.objects.get(id=snake_id)
  return render(request, 'snakes/detail.html', { 'snake': snake })

class SnakeCreate(CreateView):
  model = Snake
  fields = '__all__'

class SnakeUpdate(UpdateView):
  model = Snake
  fields = ['breed', 'description', 'age']

class SnakeDelete(DeleteView):
  model = Snake
  success_url = '/snakes/'