from django.shortcuts import render,HttpResponse
from products import sql_script
# Create your views here.

def index(request):
    return render(request,'products/main.html')

def comp(request,comp):
    companies = sql_script.distinct_companies(comp)
    desc=sql_script.intro(comp)
    return render(request,'products/products.html',{'companies':companies,'components':desc})
    