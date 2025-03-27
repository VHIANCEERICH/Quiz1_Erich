from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hi/index.html")


def erich(request):
    return HttpResponse("Hi, erich!")


def jhobs(request):
    return HttpResponse("Hi, jhobs!")


def greet(request, name):
    return render(request, "hi/greet.html", {
        "name": name.capitalize()
    })
