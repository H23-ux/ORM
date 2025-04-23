# Ex02 Django ORM Web Application
## Date: 24.04.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 movies

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

models.py

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

```



## OUTPUT

![alt text](<Screenshot 2025-04-23 170648.png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
