# imports
from django.shortcuts import render
from django.http import HttpResponse

# temp data/models
class Snake:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

snakes = [
  Snake('Kaa', 'corn snake', 'Cutie.', 3),
  Snake('Banana', 'python', 'Banan.', 0),
  Snake('Noodle', 'hognose', 'Deadly cober.', 4),
  Snake('Bonk', 'garter snake', 'Meows loudly.', 6)
]

# views
def home(request):
  return HttpResponse('<h1>Hello, Snake Collector</h1>')

def about(request):
  return render(request, 'about.html')

def snake_index(request):
  return render(request, 'snakes/index.html', { 'snakes': snakes })