from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("First django project!")