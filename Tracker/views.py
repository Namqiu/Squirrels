from django.shortcuts import render,redirect
from django.http import Http404
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


