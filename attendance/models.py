from distutils.command.upload import upload
from email.policy import default
from django.db import models
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# import sys


# Create your models here.

class college(models.Model):
    username  = models.TextField( )
    password = models.TextField( )
    name=models.TextField()
    logo = models.ImageField( upload_to="pics")
#     def save(self, *args, **kwargs):
#         imageTemproary = Image.open(self.logo)
#         outputIoStream = BytesIO()
#         imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
#         imageTemproaryResized.save(outputIoStream , format='JPEG', quality=85)
#         outputIoStream.seek(0)
#         self.logo = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.logo.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
#         super(college, self).save(*args, **kwargs)

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



