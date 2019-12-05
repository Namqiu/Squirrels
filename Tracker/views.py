import random

from django.shortcuts import render
from .models import Squirrel

def map(request):
    sightings = Squirrel.objects.all().order_by('?')[:50]
    context = {'sightings':sightings}
    return render(request,'Tracker/map.html',context)


# Create your views here.
