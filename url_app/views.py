from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(request):
    return HttpResponse("The view's great from here!")


def my_index_view(request):
    return HttpResponse("This is my second view!")


def my_hello_view(request):
    return HttpResponse("Hello from the desert of despair!")


def my_balloon_view(request):
    return HttpResponse(" 99 red balloons for you!")
