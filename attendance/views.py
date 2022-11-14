from os import link
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from attendance import models
from twilio.rest import Client
from django.contrib import messages
import random
import requests;

def institute_login(request):
    if (request.method!='POST'):
        return render(request,"login.html")

def signup(request):
    return render(request,"institute signup.html")

######################################### sign up form validation #####################################################

def submit(request):
    obj =  models.college()
    obj.username = request.POST["username"]
    obj.password = request.POST['password']
    obj.name = request.POST["instituteName"]
    obj.logo = request.FILES.get("logo","game")
    if models.college.objects.filter(username=request.POST["username"]).exists():
             return render(request,"institute signup.html",{"msg":"username exist"})
    else:
        if request.POST['password'] == request.POST['confirmPassword']:

            if models.college.objects.filter(name=request.POST["instituteName"]).exists():
                return render(request,"institute signup.html",{"msg":"institute name already exists"})
            else:
                obj.save()
                return redirect("home")
        else:
            return render(request,"institute signup.html",{"msg":"password not match"})

        
    
################################################################# login ############################################################

def login(request,id):
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']
        if request.POST["type"] == "admin":

            print("admin")
            if models.college.objects.filter(username=user).exists():
                obj = models.college.objects.get(username=user)
          
                if obj.password == passw:
                    if models.Staff.objects.filter(staffCollege=obj.name).exists():
                        data=models.Staff.objects.filter(staffCollege=obj.name)
                        return render(request,"staffAdmin.html",{"mydata":data,"logo":obj.logo.url,"userid":obj.username,"name":obj.name})
                    else:
                        
                        return render(request,"staffAdmin.html",{"logo":obj.logo.url,"userid":obj.username,"name":obj.name})
                
                else:
                    messages.info(request,"2")
                    return redirect("home")

            else:
                messages.info(request,"1")
                return redirect("home")


        else:
            print("staff")
            if  models.Staff.objects.filter(staffUsername=user).exists():
                obj =  models.Staff.objects.get(staffUsername=user)

                if obj.staffPassword == passw:
              
                    
                    obj1 = models.college.objects.get(name = obj.staffCollege)
                    return render(request,"department.html",{"name":obj1.name,"logo":obj1.logo.url,"userid":obj.staffUsername})

                else:
                    messages.info(request,"4")
                    return redirect("home")

            else:
                messages.info(request,"3")
                return redirect("home")


    else:
                print(id)
                obj = models.college.objects.get(username=id)
                data= models.Staff.objects.filter(staffCollege = obj.name)
                return render(request,"staffAdmin.html",{"mydata":data,"logo":obj.logo.url,"name":obj.name,"userid":obj.username})


    



##############################################################    years #############################################################

def year(request,user,department):
    stf = models.Staff.objects.get(staffUsername=user)
    obj1 = models.college.objects.get(name=stf.staffCollege)
    if stf.staffDep == department:
        return render(request, "year.html",{"link":department,"name":stf.staffCollege,"logo":obj1.logo.url,"userid":user})
    else:
        return render(request,"department.html",{"name":obj1.name,"logo":obj1.logo.url,"userid":stf.staffUsername,"msg":"true"})

############################################################## attendance ########################################################

def department(request,user,department,year):
    obj = models.Staff.objects.get(staffUsername=user)
    obj1 = models.college.objects.get(name=obj.staffCollege)
    student = models.Student.objects.filter(department=department,year=year,clg = obj1.name)
    years = {"1":"first year","2":"second year","3":"third year","4":"final year"}
    
    message = {"department":department,"year": years.get(str(year)),"logo":obj1.logo.url,"name":obj1.name,"detial":student,"userid":user}
    return render(request,"attendance.html",message)

                                        # # # ' ' 'STAFF ' ' ' # # #

############################################################ ADD STAFF ################################################################

def addstaffs(request,id):
    url=request.get_full_path()
    data=models.Staff.objects.all()
    obj=models.Staff()
    if request.method=='POST':

        if models.Staff.objects.filter(staffUsername=request.POST["s_username"]).exists():
            messages.info(request,"username exists")
            return redirect("admin",id)
        else:        
            obj.staffName = request.POST["s_name"]
            obj.staffDep = request.POST["s_dep"]
            obj.staffPosition = request.POST["s_position"]
            obj.staffUsername = request.POST["s_username"]
            obj.staffPassword= request.POST["s_password"]
            obj1 = models.college.objects.get(username=id)
            obj.staffCollege = obj1.name
            obj.save()
            return redirect("admin",id)
########################################################### NEW STAFF ##########################################
def newstaff(request,id):
    return render(request,"staffRegister.html")

########################################################### UPDATE ################################################################### 

def staff_update(request,id,users):
    if request.method == "POST":
       
        obj=models.Staff.objects.get(id=id)
        obj.staffName = request.POST["s_name"]
        obj.staffDep = request.POST["s_dep"]
        obj.staffPosition = request.POST["s_position"]
        obj.staffUsername = request.POST["s_username"]
        obj.staffPassword= request.POST["s_password"]
        obj.save()
        return redirect("admin",users)
    
    else:
   
        obj=models.Staff.objects.get(id=id)
        return render(request,"staffUpdate.html",{"data":obj})


########################################################## DELETE ###################################################################

def staff_delete(request,id,users):
    print("deleted")
    url=request.get_full_path()
    mydata=models.Staff.objects.get(id=id)
    mydata.delete()
    return redirect("admin",users)


                                             # # # " " " STUDENT " " " # # #


##############################################################  ADMIN  ###############################################

def admin(request,user,department,year):
    obj = models.Staff.objects.get(staffUsername=user)
    obj1 = models.college.objects.get(name=obj.staffCollege) 
    detial = models.Student.objects.filter(department=department,year=year,clg = obj1.name) 
    return render(request,"studentAdmin.html",{"logo":obj1.logo.url,"mydata":detial,"userid":obj.staffUsername,"name":obj1.name})

############################################################ UPDATE   ###############################################

def update(request,id,user,department,year):
    if request.method=='POST':
        obj = models.Student.objects.get(id=id)
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save() 
        return redirect("studentAdmin",user,department,year)
    else:
        obj = models.Student.objects.get(id=id)
        clg = models.college.objects.get(name = obj.clg)
        return render(request,"studentUpdate.html",{"data":obj,"logo":clg.logo.url,"name":clg.name,"userid":str(user)})   

######################################################### DELETE ##################################################

def delete(request,id,user,department,year):
    obj = models.Student.objects.get(id = id)
    obj.delete()
    return redirect("studentAdmin",user,department,year)

######################################################### ADD STUDENT  ##############################################

def adddata(request,user,department,year):
    obj1 = models.Staff.objects.get(staffUsername=user) 
    obj2 = models.Student()
    obj2.name = request.POST["names"]
    obj2.reg = request.POST["r_number"]
    obj2.s_mobile = request.POST["s_number"]
    obj2.p_mobile = request.POST["p_number"]
    obj2.clg = str(obj1.staffCollege)
    obj2.department = str(department) 
    obj2.year = str(year)
    obj2.save()
    return redirect("studentAdmin",user,department,year)

def newstudent(request,user,department,year,admin):
    staff = models.Staff.objects.get(staffUsername=user)
    college = models.college.objects.get(name = staff.staffCollege)
    return render(request,"studentRegister.html",{"name":college.name,"logo":college.logo.url,"userid":user,})

def back(request,user,department,year):

    return redirect("attendance",user,department,year)




##########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   SUBMIT   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################
def send(request,user,department,year):
    
    l =[]
    staf = models.Staff.objects.get(staffUsername = user)
    clg = models.college.objects.get(name=staf.staffCollege)
    obj = models.Student.objects.all().filter(department=department,year=year,clg=staf.staffCollege)
    for i in obj:
        if request.POST.get(str(i.id),False):
            i.attendance=True

    for i in obj:
        if i.attendance  == False:
            l.append(i.name)   
            number ="91"+ str(i.s_mobile)
            msg = request.POST["whatsapp"]
            msg = "*Greetings from "+clg.name +" :*"+" "+msg
            print(clg.logo.url)
            requests.get(f"https://www.ai2me.com/api/send-media.php?number={number}&msg={msg}&media=https://www.pcet.ac.in/wp-content/themes/park-theme/assets/img/park-50year-logo.png&apikey=8986051af7659d0bb239792b5e6c7c1659178e97&instance=F2P9D4o5wguLhbJ")



    
    print(l)
    return redirect("attendance",user,department,year)