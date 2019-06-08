from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json

def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse("Current server time: {now}".format(now=now))

def hi(request):
    
    string = str(request.GET)
    lst = string.split(',')

    import pdb; pdb.set_trace()
    return HttpResponse(request.GET)
    #return HttpResponse("Hi!")

    #json_var = json.dumps(request.GET)
    #for key in request.GET:
    #    json[key] = key.get(key)

    #return JsonResponse(json)
    #return JsonResponse(json_var)

def say_hi(request, name, age):

    if age < 12:
        message = "Sorry {}, you're not allowed here.".format(name)
    else:
        message = "Hello {}! Welcome to platzigram".format(name)
    return HttpResponse(message)
