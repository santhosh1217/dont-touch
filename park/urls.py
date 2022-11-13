"""park URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from attendance import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),

    path("<str:id>/admin/addnewstaff/",views.newstaff),

    path("<str:id>/admin/addnewstaff/addstaff",views.addstaffs),

    path("<str:users>/delete/<int:id>",views.staff_delete),

    path("<str:users>/update/<int:id>",views.staff_update),

    path("<str:id>/departments",views.login,name="login"),
    
    path("<str:id>/admin",views.login,name="admin"),
####################################################################### home 1 ########################################

    path("",views.institute_login,name="home"),

###################################################################### new college ###################################  

    path("signup",views.signup),


    path("submit",views.submit),

     
#######################################################################  UPDATE  ###################################

    path("<str:user>/<str:department>/<str:year>/admin/update/<int:id>",views.update),

#############################################################################  DELETE  ##################################

    path("<str:user>/<str:department>/<str:year>/admin/delete/<int:id>",views.delete),

##############################################################################  years ######################################

    path("<str:user>/<str:department>",views.year),
    
############################################################################## department #################################

    path("<str:user>/<str:department>/<str:year>/",views.department,name="attendance"),

############################################################################## edit #######################################

    path("<str:user>/<str:department>/<str:year>/admin/",views.admin,name="studentAdmin"),
    path("<str:user>/<str:department>/<str:year>/admin/back",views.back),
    
############################################################################## add student ################################

    path("<str:user>/<str:department>/<str:year>/admin/adddata",views.adddata),
    
    path("<str:user>/<str:department>/<str:year>/<str:admin>/newstudent/",views.newstudent,name="newstudent"),

     path("<str:user>/<str:department>/<str:year>/admin/newstudent/adddata",views.adddata),

   

#############################################################################  attendance #################################
    path("<str:user>/<str:department>/<str:year>/submit/",views.send),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
