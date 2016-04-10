from django.contrib import admin

# Register your models here.

from .models import workout, client, schedule


# give admin easy access to creating content for website
admin.site.register(workout)
admin.site.register(client)
admin.site.register(schedule)


