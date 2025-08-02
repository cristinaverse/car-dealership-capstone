from django.shortcuts import render
from django.http import JsonResponse
from .models import CarMake

def home(request):
    return JsonResponse({"message": "Welcome to Car Dealership!"})

def about_us(request):
    return JsonResponse({"page": "About Us", "message": "About our dealership"})

def contact_us(request):
    return JsonResponse({"page": "Contact Us", "email": "contact@dealership.com"})

def get_cars(request):
    cars = CarMake.objects.all()
    car_list = [{"name": car.name, "description": car.description} for car in cars]
    return JsonResponse(car_list, safe=False)

def get_dealers(request):
    dealers = [
        {"id": 1, "full_name": "Best Cars Kansas", "city": "Kansas City", "state": "Kansas"},
        {"id": 2, "full_name": "Auto World Kansas", "city": "Wichita", "state": "Kansas"}
    ]
    return JsonResponse(dealers, safe=False)
