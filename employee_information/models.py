from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class ToDoList(models.Model):
    title = models.TextField()
    description = models.TextField()
    duration = models.DateTimeField()


    def __str__(self):
        return self.title





class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.CharField(max_length=100,blank=True)
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=100,blank=True)
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)


    def __str__(self):
        return self.middlename + ' '+self.lastname + ' '