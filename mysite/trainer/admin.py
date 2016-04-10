from django.contrib import admin

# Register your models here.

from .models import workout # client


# give admin easy access to creating content for website
admin.site.register(workout)

# TODO add client functionality when workouts is properly working

