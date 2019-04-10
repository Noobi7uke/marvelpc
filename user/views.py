from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register(request):
    registered = False
    if request.method == 'POST':
        Name =  request.POST.get("Name")
        Email = request.POST.get("email")
        Passwd = request.POST.get("passwd")
        Mobile = request.POST.get("mobile")

        return HttpResponse("Hey %s   %s %s %s" %(Name,Email,Passwd,Mobile))
    else:
        return render(request,'user/register.html')



def login(request):
    return render(request,'user/login.html')
