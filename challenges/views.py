from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Don't eat meat for the whole month",
    "february": "Go for a 20 minute walk everyday",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Don't eat meat for the whole month",
    "may": "Go for a 20 minute walk everyday",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Don't eat meat for the whole month",
    "august": "Go for a 20 minute walk everyday",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Don't eat meat for the whole month",
    "november": "Go for a 20 minute walk everyday",
    "december": "Learn Django for at least 20 minutes a day" 
}


# Create your views here.
def monthly_challenge_by_number(request,month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!!")
        
    

