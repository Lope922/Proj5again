from django.db import models
from django.utils import timezone

# Create your models here.

class workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    # a name
    workout_name = models.CharField(max_length=25)
    # has a description #
    workout_desc = models.CharField(max_length=250)
    # number of repetitions
    reps = models.PositiveIntegerField(default=1)
    # sets
    sets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.workout_name

    #maybe later give trainer ability to select workout type
    # cardio or weight training

class client(models.Model):
    # each client is kept unique by their client id
    client_id = models.AutoField(primary_key=True)

    # Relationship of client to trainer is many to one
    # A trainer can have many clients.

    # firstname
    first_name = models.CharField(max_length=25, null=False)
    # lastname
    last_name = models.CharField(max_length=25, null=False)

    # returns the string object that is displayed in the admin page
    def __str__(self):
        return self.first_name + " " + self.last_name
    #add e-mail or phone number to contact them later


# class client_data(models.Model):
#     client_id = models.ForeignKey(client.client_id)
#     # client can have a list of appointments,
#     appointment_date = models.DateField(default=datetime.datetime.date, null=True)
#     appointment_time = models.TimeField(default=datetime.datetime.now, null=True)
    # a list of assigned workouts
    #workouts = [models.ForeignKey(workout.workout_id)]
    # assigned trainer

    # appointments
    # tuple of appointment number, with a list associated with each appointment, tied to each appointment date and time
    #appointments = [int, [appointment_date, appointment_time]]


class schedule(models.Model):

    # each appointment has a trainer mapped to a client
    trainer = models.ForeignKey('auth.User')

    appt_client = models.ForeignKey(client)

    # will have an appointment time
    appt_time = models.TimeField(default=timezone.now)
    # and an appointment date
    appt_date = models.DateField(blank=True, null=True)
    # the trainer (should be the currently logged in trainer)

    #clients ( a query for all clients that have been assigned to current trainer)

#NOTE: To activate models adjust mysite/settings. add under INSTALLED_APPS


#TODO features to possibly add are notices for personal trainers days since last visit with client
