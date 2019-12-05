from django.shortcuts import render,redirect
from django.http import Http404
from django.db.models import Count,Sum,Avg
from .models import Squirrel
from .forms import PetForm

def index(request):
    squirrel_list = Squirrel.objects.all()
    context = {'squirrel_list': squirrel_list,}
    return render(request,'Tracker/index.html',context)


def detail(request,unique_squirrel_id):
    try:
        squirrel = Squirrel.objects.get(unique_squirrel_id= unique_squirrel_id)
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel does not exist")
    if request.method == 'POST':
        form = PetForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
    else:
        form = PetForm(instance=squirrel)

    context = {'form':form,}
    return render(request, 'Tracker/detail.html',context)

def add(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/squirreltracker/sightings/')

    else:
        form = PetForm()
    context = {'form':form,}
    return render(request, 'Tracker/detail.html',context)


def map(request):
    sightings = Squirrel.objects.all().order_by('?')[:50]
    context = {'sightings':sightings}
    return render(request,'Tracker/map.html',context)

def general_stats(request):
    squirrel_list = Squirrel.objects.all()
    shift_count = squirrel_list.values('shift').annotate(count=Count('unique_squirrel_id')).values('shift','count')
    age_count = squirrel_list.values('age').annotate(count=Count('unique_squirrel_id')).values('age','count')
    primary_fur_color_count = squirrel_list.values('primary_fur_color').annotate(count=Count('unique_squirrel_id')).values('primary_fur_color','count')
    location_count = squirrel_list.values('location').annotate(count=Count('unique_squirrel_id')).values('location','count')
    running_count = squirrel_list.values('running').annotate(count=Count('unique_squirrel_id')).values('running','count')
    context = {
        "shift_count":shift_count,
        "age_count":age_count,
        "primary_fur_color_count":primary_fur_color_count,
        "location_count":location_count,
        "running_count":running_count,
    }
    return render(request, 'Tracker/stats.html',context)

