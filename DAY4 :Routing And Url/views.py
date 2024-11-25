from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# def work(request):
#     return HttpResponse("<h1>This is the work route")

# def chores(request):
#     # Create your views here.
# def school(request):
#     return HttpResponse
def task(request,place):
    if place=="school":
        task="<ul><li>do your homework</li><li>Do the cat</li><li>write report paper</li>"
    elif place=="home":
        task="<h1>Home Tasks are : </h1><ul><li>Do the dishes</li><li>Clean the house</li> <li>Do the laundry</li>"
    elif place=="workPlace":
        task="<h1>Work Tasks are : </h2><ul><li>Send email</li><li>submit report</li><li>contact HR</li></ul>"
    else:
        return HttpResponseNotFound("No tasks to specified path")
    return HttpResponse(task)