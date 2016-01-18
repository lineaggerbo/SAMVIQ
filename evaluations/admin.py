from django.contrib import admin
from .models import Observer
from .models import Image
from .models import Rating

# Register your models here.

admin.site.register(Observer)
admin.site.register(Image)
admin.site.register(Rating)