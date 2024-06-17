from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def list_item(request):
    return HttpResponse("hello")
