from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from APP_ESPORTS.forms import *
from APP_ESPORTS.models import *

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# def typeList(request):
#     typelist = TypeList.objects.all().order_by()
#     context = {'raceType': typelist}
#     return render(request,"raceType.html",context)
#
# def director(request):
#     direc = Director.objects.all().order_by()
#     context = {'direc':direc}
#     return render(request,"director.html",context)
#
# def ageCategory(request):
#     age = AgeCategory.objects.all().order_by()
#     context = {'age':age}
#     return render(request,"ageCategory.html",context)
#
# def season(request):
#     sea = Season.objects.all().order_by()
#     context = {'sea':sea}
#     return render(request,"season.html",context)
#
# def base(request):
#     return render(request,"base.html")
#

#
# def team(request):
#     teamList = Team.objects.all().order_by()
#     context = {'teamList': teamList}
#     return render(request, "team.html", context)
#
def createTeam(request):
    if request.method == 'POST':
        form = TeamFrom(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team')
        else:
            context = {'form': form}
            return render(request, 'CRUD/createTeam.html', context)
    else:
        form = TeamFrom()
        context = {'form': form}
        return render(request, 'CRUD/createTeam.html', context)

def form_team(request):
    return render(request,"form_team.html")


#AGE CATE GORY
def ageCategory(request):
    age = AgeCategory.objects.all().order_by()
    context = {'age':age}
    return render(request,"ageCategory.html",context)

def newAgeCategory(request):
    if request.method == 'POST':
        form = AgeCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ageCategory')
        else:
            context = {'form': form}
            return render(request, 'CRUD/AgeCategoryNew.html', context)
    else:
        form = AgeCategoryForm()
        context = {'form': form}
        return render(request, 'CRUD/AgeCategoryNew.html', context)

def updateAgeCategory(request, id):
    agecategory = get_object_or_404(AgeCategory, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=agecategory)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ageCategory')
        else:
            context = {'form': form}
            return render(request, 'CRUD/AgeCategoryUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/AgeCategoryUpdate.html', context)

def deleteAgeCategory(request, id):
    agecategory = get_object_or_404(AgeCategory, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=agecategory)
    if request.method == 'POST':
        agecategory.delete()
        return redirect('ageCategory')
    else:
        form.deleteForm()
        context = {'form': form, 'agecategory': agecategory}
        return render(request, 'CRUD/AgeCategoryDelete.html', context)



#SEASON
def season(request):
    sea = Season.objects.all().order_by()
    context = {'sea':sea}
    return render(request,"season.html",context)
def newSeason(request):
    if request.method == 'POST':
        form = SeasonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('season')
        else:
            context = {'form': form}
            return render(request, 'CRUD/SeasonNew.html', context)
    else:
        form = AgeCategoryForm()
        context = {'form': form}
        return render(request, 'CRUD/SeasonNew.html', context)

def updateSeason(request, id):
    seasons = get_object_or_404(Season, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=seasons)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('season')
        else:
            context = {'form': form}
            return render(request, 'CRUD/SeasonUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/SeasonUpdate.html', context)

def deleteSeasaon(request, id):
    seasons = get_object_or_404(Season, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=seasons)
    if request.method == 'POST':
        seasons.delete()
        return redirect('season')
    else:
        form.deleteForm()
        context = {'form': form, 'season': seasons}
        return render(request, 'CRUD/SeasonDelete.html', context)

def base(request):
    return render(request,"base.html")

#DIRECTOR กรรมการ
def director(request):
    direc = Director.objects.all().order_by()
    context = {'direc':direc}
    return render(request,"director.html",context)

def newDirector(request):
    if request.method == 'POST':
        form = DirectorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('director')
        else:
            context = {'form': form}
            return render(request, 'CRUD/DirectorNew.html', context)
    else:
        form = DirectorForm()
        context = {'form': form}
        return render(request, 'CRUD/DirectorNew.html', context)

def updateDirector(request, id):
    director = get_object_or_404(Director, id=id)
    form = DirectorForm(data=request.POST or None, instance=director)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('director')
        else:
            context = {'form': form}
            return render(request, 'CRUD/DirectorUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/DirectorUpdate.html', context)

def deleteDirector(request, id):
    director = get_object_or_404(Director, id=id)
    form = DirectorForm(data=request.POST or None, instance=director)
    if request.method == 'POST':
        director.delete()
        return redirect('director')
    else:
        form.deleteForm()
        context = {'form': form, 'typelist': director}
        return render(request, 'CRUD/DirectorDelete.html', context)
#TYPE
def typeList(request):
    typelist = TypeList.objects.all().order_by()
    context = {'raceType': typelist}
    return render(request,"raceType.html",context)
def newRaceType(request):
    if request.method == 'POST':
        form = RaceTypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('raceType')
        else:
            context = {'form': form}
            return render(request, 'CRUD/RaceTypeNew.html', context)
    else:
        form = RaceTypeForm()
        context = {'form': form}
        return render(request, 'CRUD/RaceTypeNew.html', context)

def updateRaceType(request, id):
    typelist = get_object_or_404(TypeList, id=id)
    form = RaceTypeForm(data=request.POST or None, instance=typelist)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('raceType')
        else:
            context = {'form': form}
            return render(request, 'CRUD/RaceTypeUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/RaceTypeUpdate.html', context)

def deleteRaceType(request, id):
    typelist = get_object_or_404(TypeList, id=id)
    form = RaceTypeForm(data=request.POST or None, instance=typelist)
    if request.method == 'POST':
        typelist.delete()
        return redirect('raceType')
    else:
        form.deleteForm()
        context = {'form': form, 'typelist': typelist}
        return render(request, 'CRUD/RaceTypeDelete.html', context)

def team(request):
    teamList = Team.objects.all().order_by()
    context = {'teamList': teamList}
    return render(request, "team.html", context)

def team_table(request):
    teamVslist = TeamVs.objects.all().order_by()
    context = {'teamVslist': teamVslist}
    return render(request, "team_table.html", context)


# def createTeam(request):
#     if request.method == 'POST':
#         form = TeamFrom(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('team')
#         else:
#             context = {'form': form}
#             return render(request, 'CRUD/createTeam.html', context)
#     else:
#         form = TeamFrom()
#         context = {'form': form}
#         return render(request, 'CRUD/createTeam.html', context)

def updateTeam(request, id):
    teams = get_object_or_404(Team, id = id)
    form = TeamFrom(data=request.POST or None, instance = teams)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('team')
        else:
            context = {'form': form}
            return render(request,'CRUD/updateTeam.html' )
    else:
        context = {'form': form}
        return render(request, 'CRUD/updateTeam.html', context)

def deleteTeam(request, id):
    teams = get_object_or_404(Team, id = id)
    form = TeamFrom(data=request.POST or None, instance=teams)
    if request.method == 'POST':
        teams.delete()
        return redirect('team')
    else:
        form.deleteForm()
        context = {'form': form, 'teams': teams}
        return render(request, 'CRUD/deleteTeam.html', context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if confirmpassword == password:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            user.is_staff = False
            return redirect('signin')
        else:
            return render(request,'singup.html')
    else:
        return render(request,'singup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'team.html', {'fname': fname})
        else:
            messages.error(request, "BAD")
            return redirect('signin')
    else:
        return render(request, 'signin.html')



def userlogout(request):
    logout(request)
    return redirect('base')


def teamNew(request):
    teamList1 = Team.objects.all().order_by()
    context = {'teamList1': teamList1}
    return render(request, "teamNew.html", context)
