from django.conf.urls import url
from . import views

urlpatterns = [

    # the index page should display all of the information about the current logged in Trainer
    url(r'^$', views.index, name='index'),


    url(r'^newWorkout', views.create, name='create'),


    url(r'^schedule', views.schedule, name='schedule'),


    url(r'^assign', views.assign, name='assign'),


    url(r'^Workouts', views.workout, name='workout'),

    # this url is used to display test urls
    url(r'^test', views.test, name='test'),

]