# imports
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Snake
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'snakes/detail.html', {
    'snake': snake, 'feeding_form': feeding_form
  })

class SnakeCreate(CreateView):
  model = Snake
  fields = '__all__'

class SnakeUpdate(UpdateView):
  model = Snake
  fields = ['breed', 'description', 'age']

class SnakeDelete(DeleteView):
  model = Snake
  success_url = '/snakes/'