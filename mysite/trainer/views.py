from django.shortcuts import render , redirect
from .models import workout

from django.http import HttpResponse

# i may have been stuck because of missing this for the longest. like 4 hours easily.
from .models import workout
# Create your views here.


# later modify this index to display are the trainer abilities
def index(request):
   # return HttpResponse("Hello this would be the Welcome page  ")

    # returns a query set of just the values requested.
    v = workout.objects.values('workout_id', 'workout_name', 'sets', 'reps')
    # the flat true returns a flat list of values instead of a queryset/ dict
    # returns just a list not a dict
    workout_w_rep_and_sets = workout.objects.values("reps", "sets", "workout_name")
    just_names = workout.objects.values_list('workout_name', flat=True)
    context2 = {'bunch': workout_w_rep_and_sets}
    context3 = {'just names': just_names}
    return render(request, "WelcomePage.html", context2)



def create(request):
    return HttpResponse("This page is where you will create workouts")


def assign(request):
    return HttpResponse("Here is where you will assign a workout routine")


def schedule(request):
    return HttpResponse("Here is where Trainers can view their schedule, and reschedule if needed ")


def list_workouts(request, context2):
    return render(request, "WelcomePage.html", context2)
    # workout_list = workout.objects.all()
    # return HttpResponse(workout_list)


def test(request, context3):
    workout_list = workout.objects.values_list("workout_name", flat=True)
    context = {'all workout names': workout_list}
    return render(request, 'workout_list_avail.html', context)
