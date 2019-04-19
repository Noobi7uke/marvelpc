from django.shortcuts import render,HttpResponse,redirect
from user.sql_script import user_info
from rig import sql_script
# Create your views here.

def index(request):
    if request.method == "POST":
        print(request.POST['action'])
        if request.POST['action'].split("|")[0]=='add':
            return redirect('/rig/%s/add' %(request.POST['action'].split("|")[1]))
        elif request.POST['action'].split("|")[0]=='change':
            return redirect('/rig/%s/%s/%s/change' %(request.POST['action'].split("|")[2],request.POST['rig'],request.POST['action'].split("|")[1]))
        else:
            return remove(request.POST['rig'],request.POST['action'].split('|')[1])
    else:
        dic = sql_script.get_rig(request)
        dic.update(user_info(request))
        return render(request,'rig/rig.html',context=dic)

def add(request,Type=None):
    if not sql_script.check(request,Type):
         return HttpResponse(Type+" is already in your Rig.")

    if request.method == 'POST':
        sql_script.add(request)
        return redirect('/rig/home')
    
    else:
        dic = {}
        dic['products'] = sql_script.show(request,Type)
        dic.update(user_info(request))
        return render(request,'rig/rig_inven.html',dic)
    #return HttpResponse(request.POST['rig']+'  '+request.POST['action'].split('|')[0]+ "        " + request.POST['action'].split('|')[1])
    

def change(request,Type,Rig,Inven):
    #return HttpResponse(request.POST['rig']+'  '+request.POST['action'].split('|')[0]+ "        " + request.POST['action'].split('|')[1])
    if request.method == 'POST':
        sql_script.add(request)
        return redirect('/rig/home')
    else:
        sql_script.remove(Rig,Inven)
        dic = {'rig_msg':Type+' is removed from Rig Chose another '+ Type}
        dic['products'] = sql_script.show(request,Type)
        dic.update(user_info(request))
        return render(request,'rig/rig_inven.html',dic)
    

def remove(Rig,Inven):
    sql_script.remove(Rig,Inven)
    #return HttpResponse(request.POST['rig']+'  '+request.POST['action'].split('|')[0]+ "        " + request.POST['action'].split('|')[1])
    return redirect('/rig/home')

