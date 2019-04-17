from django.shortcuts import render,HttpResponse
from user.sql_script import user_info
from rig.sql_script import get_rig
# Create your views here.

def index(request):
    dic = get_rig(request)
    dic.update(user_info(request))
    return render(request,'rig/rig.html',context=dic)

def add(request,Type):
    return HttpResponse('%s' %(Type))

def change(request,Type):
    
    return HttpResponse('%s' %(Type))
    