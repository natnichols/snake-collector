# imports
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Snake, Hide, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'nn-snake-collector'

# views
def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('snake-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

@login_required
def snake_index(request):
  snakes = Snake.objects.filter(user=request.user)
  return render(request, 'snakes/index.html', { 'snakes': snakes })

@login_required
def snake_detail(request, snake_id):
  snake = Snake.objects.get(id=snake_id)
  feeding_form = FeedingForm()
  hides_snake_doesnt_have = Hide.objects.exclude(id__in = snake.hides.all().values_list('id'))
  return render(request, 'snakes/detail.html', {
    'snake': snake, 'feeding_form': feeding_form, 'hides': hides_snake_doesnt_have
  })

def add_photo(request, snake_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, snake_id=snake_id)
      snake_photo = Photo.objects.filter(snake_id=snake_id)
      if snake_photo.first():
        snake_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occured uploading file to S3: %s' % err)
  return redirect('snake-detail', snake_id=snake_id)

@login_required
def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('snake-detail', snake_id=snake_id)

@login_required
def assoc_hide(request, snake_id, hide_id):
  Snake.objects.get(id=snake_id).hides.add(hide_id)
  return redirect('snake-detail', snake_id=snake_id)

class Home(LoginView):
  template_name = 'home.html'

class SnakeCreate(LoginRequiredMixin, CreateView):
  model = Snake
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SnakeUpdate(LoginRequiredMixin, UpdateView):
  model = Snake
  fields = ['breed', 'description', 'age']

class SnakeDelete(LoginRequiredMixin, DeleteView):
  model = Snake
  success_url = '/snakes/'

class HideCreate(LoginRequiredMixin, CreateView):
  model = Hide
  fields = '__all__'

class HideList(LoginRequiredMixin, ListView):
  model = Hide

class HideDetail(LoginRequiredMixin, DetailView):
  model = Hide

class HideUpdate(LoginRequiredMixin, UpdateView):
  model = Hide
  fields = ['name', 'color']

class HideDelete(LoginRequiredMixin, DeleteView):
  model = Hide
  success_url = '/hides/'