from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("Swidt Account detail will be diplayed here")