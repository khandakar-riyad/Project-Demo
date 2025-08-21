from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("This is App HOme page")
    
def home(request):
    return JsonResponse({"message": "This is new Bangladesh"})

    