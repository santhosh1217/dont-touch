from distutils.command.upload import upload
from email.policy import default
from django.db import models
from PIL import Image


# Create your models here.

class college(models.Model):
    username  = models.TextField( )
    password = models.TextField( )
    name=models.TextField()
    logo = models.ImageField( upload_to="pics")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img =Image.open(self.logo.path)
        if img.height > 100 or img.weight >100:
            output_size = (100, 100)
            img.thumbnail (output_size)
            img.save(self.logo.path)

class Student(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.TextField()
    p_mobile = models.TextField()
    attendance = models.BooleanField(default=False)
    clg = models.TextField()
    department = models.TextField()
    year = models.TextField()

class Staff(models.Model):
    staffName=models.TextField()
    staffDep=models.TextField()
    staffCollege = models.TextField()
    staffPosition=models.TextField()
    staffUsername=models.TextField()
    staffPassword=models.TextField()



