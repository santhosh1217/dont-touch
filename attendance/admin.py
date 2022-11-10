from django.contrib import admin
from attendance import models

# Register your models here.
admin.site.register(models.college)
admin.site.register(models.Staff)
admin.site.register(models.Student)

