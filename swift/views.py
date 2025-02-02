from django.shortcuts import render
# from . import swiftForm
from django.contrib import messages

# Create your views here.
def swiftAccountDetail(request):
    return render(request, "index.html")