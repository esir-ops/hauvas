from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def todo_page(request):
    return HttpResponse("Todo")
