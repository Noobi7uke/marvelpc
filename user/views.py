from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from user.models import UserProfile
from user.forms import UserForm,UserProfileForm
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
        address = request.POST.get("address")+request.POST.get("city")+request.POST.get("state")
        print(Name,Email,DOB_date+'-'+DOB_month+'-'+DOB_year,address)
        user = User(username=Name,email=Email)
        user.set_password(Passwd)
        user.save()
        registered = True
        return redirect('/')
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request,'user/register.html',{'States':States_DIC,'registered':registered})



def user_login(request):
    return render(request,'user/login.html')
