from django.shortcuts import render
from django.http import HttpResponse

# Views:
def home(request):
  return HttpResponse('<h1>Hello, Snake Collector</h1>')

def about(request):
  return render(request, 'about.html')