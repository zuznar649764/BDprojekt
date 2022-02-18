from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('rejestracja/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('calendar/', views.calendar, name='calendar'),
    path('addCompetition/', views.addCompetition, name ='addCompetition'),
    path('addTraining/', views.addTraining, name ='addTraining'),
    path('allEvents/', views.allEvents, name ='allEvents'),
    path('allTrainings/', views.allTrainings, name ='allTrainings'),

]