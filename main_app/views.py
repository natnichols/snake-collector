# imports
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Snake, Hide
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

def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('snake-detail', snake_id=snake_id)

class SnakeCreate(CreateView):
  model = Snake
  fields = '__all__'

class SnakeUpdate(UpdateView):
  model = Snake
  fields = ['breed', 'description', 'age']

class SnakeDelete(DeleteView):
  model = Snake
  success_url = '/snakes/'

class HideCreate(CreateView):
  model = Hide
  fields = '__all__'

class HideList(ListView):
  model = Hide

class HideDetail(DetailView):
  model = Hide

class HideUpdate(UpdateView):
  model = Hide
  fields = ['name', 'color']

class HideDelete(DeleteView):
  model = Hide
  success_url = '/hides/'