from django.shortcuts import render

from APP_ESPORTS.models import *


# Create your views here.

def typeList(request):
    raceType = typeList.objects.all().order_by()
    context = {'raceType': typeList}
    return render(request,"raceType.html",context)

def director(request):
    director = Director.objects.all().order_by()
    context = {'categories':RaceType}
    return render(request,"director.html",context)

def base(request):
    return render(request,"base.html")

def newRaceType(request):
    return render(request,"CRUD/newRaceType.html")


