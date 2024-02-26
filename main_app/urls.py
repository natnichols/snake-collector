# imports
from django.urls import path
from . import views

# views
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('snakes/', views.snake_index, name='snake-index'),
]
