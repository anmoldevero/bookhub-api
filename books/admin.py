from django.contrib import admin

# Register your models here.
from .models import Book, Like, Comment



admin.site.register([Book, Like, Comment])


