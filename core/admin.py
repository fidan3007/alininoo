from django.contrib import admin
from core.models import *
admin.site.register({Product, Tag, Book, Toy, Technique, News, Club, Slider, Category, Event,Comment})
