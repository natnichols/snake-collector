from django.contrib import admin
from .models import Snake, Feeding, Hide, Photo

# Register your models here.
admin.site.register(Snake)
admin.site.register(Feeding)
admin.site.register(Hide)
admin.site.register(Photo)