from distutils.command.upload import upload
from email.policy import default
from django.db import models


# Create your models here.
class college(models.Model):
    username  = models.CharField( max_length=50)
    password = models.CharField( max_length=20)
    name=models.TextField()
    logo = models.ImageField( upload_to="pics")

class Student(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)
    clg = models.TextField()
    department = models.TextField()
    year = models.TextField()

class Staff(models.Model):
    staffName=models.TextField(max_length=50)
    staffDep=models.TextField(max_length=40)
    staffCollege = models.TextField()
    staffPosition=models.TextField(max_length=20)
    staffUsername=models.TextField(max_length=20)
    staffPassword=models.TextField(max_length=20)



