from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the whole month")

def february(request):
    return HttpResponse("Walk for at least 20 minutes per day")

def march(request):
    return HttpResponse("Learn Django for 20 minutes every day")

def monthly_challenges(request, month):
    challenge_text = None
    
    if month == "january":
        challenge_text = "Eat no meat for the whole month"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes per day"
    elif month == "march":
        challenge_text = "Learn Django for 20 minutes every day"
    else:
        return HttpResponseNotFound("This month is currently not supported")

    return HttpResponse(challenge_text)

