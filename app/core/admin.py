from django.contrib import admin
from . models import User, Recipe

admin.site.register(User)
admin.site.register(Recipe)