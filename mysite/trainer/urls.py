from django.conf.urls import url
from . import views

urlpatterns = [

    # the index page should display all of the information about the current logged in Trainer
    url(r'^$', views.index, name='index'),

    # not implemented yet for now this is acheived through admin site
    url(r'^newWorkout', views.create, name='create'),

    # implemented but needs refining
    url(r'^schedule', views.appointments, name='schedule'),


    # this url is where the Trainer will assign their clients their workout program
    url(r'^assign', views.assign, name='assign'),

    # not implemented yet displays list of clients for trainer to checkup on
    url('r^checkup', views.checkup, name='checkup'),
]