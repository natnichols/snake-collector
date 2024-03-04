# imports
from django.urls import path
from . import views

# routes
urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('snakes/', views.snake_index, name='snake-index'),
  path('snakes/<int:snake_id>/', views.snake_detail, name='snake-detail'),
  path('snakes/create/', views.SnakeCreate.as_view(), name='snake-create'),
  path('snakes/<int:pk>/update/', views.SnakeUpdate.as_view(), name='snake-update'),
  path('snakes/<int:pk>/delete/', views.SnakeDelete.as_view(), name='snake-delete'),
  path('snakes/<int:snake_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('snakes/<int:snake_id>/add-photo/', views.add_photo, name='add-photo'),
  path('snakes/<int:snake_id>/assoc-hide/<int:hide_id>/', views.assoc_hide, name='assoc-hide'),
  path('hides/create/', views.HideCreate.as_view(), name='hide-create'),
  path('hides/<int:pk>/', views.HideDetail.as_view(), name='hide-detail'),
  path('hides/', views.HideList.as_view(), name='hide-index'),
  path('hides/<int:pk>/update/', views.HideUpdate.as_view(), name='hide-update'),
  path('hides/<int:pk>/delete/', views.HideDelete.as_view(), name='hide-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
