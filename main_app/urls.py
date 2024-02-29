# imports
from django.urls import path
from . import views

# views
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('snakes/', views.snake_index, name='snake-index'),
  path('snakes/<int:snake_id>/', views.snake_detail, name='snake-detail'),
  path('snakes/create/', views.SnakeCreate.as_view(), name='snake-create'),
  path('snakes/<int:pk>/update/', views.SnakeUpdate.as_view(), name='snake-update'),
  path('snakes/<int:pk>/delete/', views.SnakeDelete.as_view(), name='snake-delete'),
  path('snakes/<int:snake_id>/add-feeding/', views.add_feeding, name='add-feeding'),
]
