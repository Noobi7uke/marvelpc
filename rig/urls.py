from django.conf.urls import url
from rig import views
from django.urls import path

urlpatterns = [
    path('home',views.index,name='index'),
    path('<str:Type>/<str:Rig>/<str:Inven>/change',views.change,name="change"),
    path('<str:Type>/add',views.add,name="add"),
    
]