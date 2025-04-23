from django.db import models
from django.contrib import admin
class Movie (models.Model):
    Movieeid=models.IntegerField(primary_key=True)
    Moviename=models.CharField(max_length=100)
    Price_of_tickets=models.IntegerField()
    No_of_tickets=models.IntegerField()
    Genre=models.CharField()
 
class MovieAdmin(admin.ModelAdmin):
    list_display=('Movieeid','Moviename','Price_of_tickets','No_of_tickets','Genre')
