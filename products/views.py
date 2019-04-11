from django.shortcuts import render,HttpResponse
from products import sql_script
# Create your views here.

def index(request):
    return render(request,'products/main.html')

def comp(request,comp):
    companies = sql_script.distinct_companies(comp)
    companies_chosen = {}
    for c in companies:
        companies_chosen[c]=False
    if request.method=='POST':
        companies_required = []
        for i in companies:
            if request.POST.get(i) == 'on':
                companies_required.append(i)
                companies_chosen[i]=True
        desc = sql_script.intro(comp,companies=companies_required)
    else:
        desc=sql_script.intro(comp)
    dic = {'companies':companies,'components':desc}
    dic.update(companies_chosen)
    print(dic)
    return render(request,'products/products.html',dic)

def item(request,comp,product):
    dic = sql_script.sel_item(product)
    print(dic)
    return render(request,'products/item.html',dic)