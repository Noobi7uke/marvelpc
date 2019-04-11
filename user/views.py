from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout


from user import sql_script
# Create your views here.
from json import loads
from os import path


BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
file = path.join(BASE_DIR,"user","StatesIndia.json")
States_DIC = loads(open(file).read())


from django.contrib.auth.models import User

def user_register(request):
    registered = False
    if request.user.is_authenticated:
        return HttpResponse("You are already Logged in")
    if request.method == 'POST' and not request.user.is_authenticated:
        Name =  request.POST.get("Name")
        Email = request.POST.get("email")
        Passwd = request.POST.get("passwd")
        Mobile = request.POST.get("mobile")
        DOB_date = request.POST.get("birth_year_day")
        DOB_month = request.POST.get("birth_year_month")
        DOB_year = request.POST.get("birth_year_year")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        #print(Name,Email,DOB_date+'-'+DOB_month+'-'+DOB_year,address)
        errors = {'err':False,'username':False,'email':False,'address':False,'city':False,'state':False,'pincode':False,'phone':False}
        errors = sql_script.check_for_user(Name,Email,errors)
        errors = sql_script.check_for_customer(Name,Email,Mobile,errors)
        #print(errors)
        if errors['err']==False:
            user = User(username=Name,email=Email)
            user.set_password(Passwd)
            user.save()
            id = sql_script.select("SELECT id FROM auth_user WHERE email = %s ",(Email,))[0][0]
            print(id)
            sql_script.insert_to_customer(Name,Email,address,city,state,"110025",Mobile,id)
            registered = True
            return HttpResponse("<p>You are registered</p><a href ='/'>Home</a> ")
        else:
            return render(request,'user/register.html',{'States':States_DIC,'registered':registered,'errors':errors})    

        
    else:
        return render(request,'user/register.html',{'States':States_DIC,'registered':registered})



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("You are not active user")
        else:
            return render(request,'user/login.html')
    else:
        return render(request,'user/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
