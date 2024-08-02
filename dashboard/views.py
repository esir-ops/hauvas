from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard_test(request):
    return HttpResponse("Tite")
