from django.db import models
import datetime

# Create your models here.

class workout(models.Model):
    # a name
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=25)
    # has a description
    workout_desc = models.CharField(max_length=250)
    # number of repetitions
    reps = models.PositiveIntegerField(default=1)
    # sets
    sets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.workout_name
    #maybe later give trainer ability to select workout type
    # cardio or weight training

# class schedule(models.Model):
#

#     # will have an appointment time
#     appt_time = models.TimeField
#     # and an appointment date
#     appt_date = models.DateField
#     # the trainer (should be the currently logged in trainer)
#
#     #clients ( a query for all clients that have been assigned to current trainer)

# NOTE: To activate models adjust mysite/settings. add under INSTALLED_APPS

# class client(models.Model):
#     # client can have a list of appointments,
#     appointment_date = models.DateField(default=datetime.datetime.date(), null=True)
#     appointment_time = models.TimeField(default=datetime.datetime.now(), null=True)
#     # a list of assigned workouts
#     workouts = []
#     # assigned trainer
#
#     # appointments
#     # tuple of appointment number, with a list associated with each appointment, tied to each appointment date and time
#     appointments = [int, [appointment_date, appointment_time]]
#     # firstname
#     first_name = models.CharField(max_length=25, null=False)
#     # lastname
#     last_name = models.CharField(max_length=25, null=False)


