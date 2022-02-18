from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
TRAININGS = (
    ('Trening ujeżdżeniowy', 'Trening ujeżdżeniowy'),
    ('Trening skokowy', 'Trening skokowy'),
    ('jazda rekreacyjna', 'jazda rekreacyjna'),
    ('wyjazd w teren', 'wyjazd w teren'),
    ('inne', 'inne'),

)

COMPETITIONS = (
    ('Zawody w ujeżdżeniu', 'Zawody w ujeżdżeniu'),
    ('Zawody w skokach', 'Zawody w skokach'),
    ('inne', 'inne'),

)

LEVELS = (
    ('L', 'L'),
    ('P', 'P'),
    ('N', 'N'),
    ('C', 'C'),
    ('inne', 'inne'),


)

FUNCTIONS = (
    ('trener ujeżdżenia', 'trener ujeżdżenia'),
    ('trener skoków', 'trener skoków'),
    ('instruktor rekreacji', 'instruktor rekreacji'),
    ('stajenny', 'stajenny'),
    ('pracownik', 'pracownik'),
    ('właściciel ośrodka', 'właściciel ośrodka'),

)

class Horse(models.Model):
    name = models.CharField(max_length=255)
    specification = models.TextField()
    height = models.DecimalField(max_digits=5, decimal_places=1)
    breed = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    function = models.CharField(max_length=255, choices= FUNCTIONS)
    def __str__(self):
        return self.name


class Training(models.Model):
    type = models.CharField(max_length=255, choices= TRAININGS)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    owner = models.ManyToManyField(Employee)
    horses = models.ManyToManyField(Horse)
    members = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.type



class CompetionLevel(models.Model):
    name = models.CharField(max_length=255, choices=LEVELS, unique=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.CharField(max_length=255, choices=COMPETITIONS)
    levels = models.ManyToManyField(CompetionLevel)
    owner = models.ManyToManyField(Employee)


    def __str__(self):
        return self.title






