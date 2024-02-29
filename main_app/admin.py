from django.contrib import admin
from .models import Snake, Feeding, Hide

# Register your models here.
admin.site.register(Snake)
admin.site.register(Feeding)
admin.site.register(Hide)
