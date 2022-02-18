from django.contrib import admin
from .models import Horse, Competition, CompetionLevel, Training, Employee

admin.site.register(Horse)
admin.site.register(Competition)
admin.site.register(CompetionLevel)
admin.site.register(Training)
admin.site.register(Employee)


# Register your models here.
