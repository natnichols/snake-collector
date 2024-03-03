# imports
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Snake, Hide
from .forms import FeedingForm

# views
def about(request):
  return render(request, 'about.html')

def snake_index(request):
  snakes = Snake.objects.all()
  return render(request, 'snakes/index.html', { 'snakes': snakes })

def snake_detail(request, snake_id):
  snake = Snake.objects.get(id=snake_id)
  feeding_form = FeedingForm()
  hides_snake_doesnt_have = Hide.objects.exclude(id__in = snake.hides.all().values_list('id'))
  return render(request, 'snakes/detail.html', {
    'snake': snake, 'feeding_form': feeding_form, 'hides': hides_snake_doesnt_have
  })

def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('snake-detail', snake_id=snake_id)

def assoc_hide(request, snake_id, hide_id):
  Snake.objects.get(id=snake_id).hides.add(hide_id)
  return redirect('snake-detail', snake_id=snake_id)

class Home(LoginView):
  template_name = 'home.html'

class SnakeCreate(CreateView):
  model = Snake
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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