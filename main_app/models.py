from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

MEALS = (
  ('P', 'Pinky'),
  ('F', 'Fuzzy'),
  ('H', 'Hopper'),
)

# Create your models here.
class Hide(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('hide-detail', kwargs={"pk": self.id})

class Snake(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  hides = models.ManyToManyField(Hide)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('snake-detail', kwargs={'snake_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  snake = models.ForeignKey(Snake, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  snake = models.OneToOneField(Snake, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for snake_id: {self.snake_id} @{self.url}"