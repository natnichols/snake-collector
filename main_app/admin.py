from django.contrib import admin
from .models import Snake
# Register your models here.
admin.site.register(Snake)

# git commit -m 'create superuser, import Snake model into main_app admin, register Snake model with admin'