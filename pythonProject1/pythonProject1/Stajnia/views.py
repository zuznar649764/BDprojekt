from django.shortcuts import render
from .models import Horse, Competition, CompetionLevel, Training, Employee
from .forms import MyRegisterForm, AddCompetionForm, AddTrainingForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
import json
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def allEvents(request):
    competitions = Competition.objects.all()
    competition_list = []

    for competition in competitions:
        competition_list.append({"title": competition.title,
                                 "start": competition.start_time})


    context = {"competitions": competition_list}
    return render(request, 'allEvents.html', context)

def allTrainings(request):
    trainings = Training.objects.all()
    training_list = []

    for training in trainings:
        training_list.append({"type": training.type,
                              "start": training.start_time})

    context = {"trainings": training_list}
    return render(request, 'allTrainings.html', context)

def calendar(request):

    competitions = Competition.objects.all()
    competition_list = []

    for competition in competitions:
        competition_list.append({"title": competition.title,
                                 "start": competition.start_time.date().strftime("%Y-%m-%dT%H:%M:%S"),
                                 "end": competition.end_time.date().strftime("%Y-%m-%dT%H:%M:%S"),
                                 })
    context = {"competitions": competition_list}

    return render(request, 'calendar.html', context)

def addCompetition(request):
    form = AddCompetionForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'addCompetition.html', context)

def addTraining(request):
    form = AddTrainingForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'addTraining.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = MyRegisterForm()
        if request.method == 'POST':
            form = MyRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + user + ' created successfully')
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Incorrect username or password')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

