from django.shortcuts import render , redirect
from .models import workout , client , schedule

from django.http import HttpResponse

# i may have been stuck because of missing this for the longest. like 4 hours easily.
from .models import workout
# Create your views here.


# later modify this index to display are the trainer abilities
def index(request):
   # return HttpResponse("Hello this would be the Welcome page  ")

    # returns a query set of just the values requested.
   # v = workout.objects.values('workout_id', 'workout_name', 'sets', 'reps')
    # the flat true returns a flat list of values instead of a queryset/ dict
    # returns just a list not a dict
    workout_w_rep_and_sets = workout.objects.values("workout_name", "reps", "sets")
    just_names = workout.objects.values_list('workout_name', flat=True)

    context2 = {'bunch': workout_w_rep_and_sets}
    context3 = {'just_names': just_names}
    return render(request, "WelcomePage.html", context2)

def create(request):
    return HttpResponse("This page is where you will create workouts")

# assigning workouts to clients
def assign(request):

    #Todo later check and make sure if clients are assigned trainers or not.
    c = client.objects.all()
    client_query = {'client_query': c}
    #TODO allow trainer to assign workouts from list and update reps and set here

    return render(request, "AssignWorkouts.html", client_query)
    #return HttpResponse("Here is where you will assign a workout routine")

# not implemented yet
def checkup(request):
    return render(request, 'ClientCheckup.html')

# TODO ADJUST QUERY TO CHECK FOR APPOINTMENTS THAT ARE BEFORE TODAY. ALSO sort query by date
def appointments(request):
    sched_appts = schedule.objects.values('appt_date', 'appt_time', 'appt_client')
    appoint_dict = {'appointments':sched_appts}
    #return HttpResponse("Here is where Trainers can view their schedule, and reschedule if needed ", {'sched_appt':appoint_dict})
    return render(request, 'schedule.html',appoint_dict)

