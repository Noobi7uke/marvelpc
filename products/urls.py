from django.conf.urls import url,include
from products import views
from django.urls import path
urlpatterns = [
    path('',views.index,name="index"),
    path('main/',views.index,name='index'),
    path('<str:comp>/',views.comp,name="component"),
    path('<str:comp>/<str:product>/',views.item,name="product")
]