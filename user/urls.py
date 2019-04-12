from django.conf.urls import url
from user import views
from django.urls import path

urlpatterns = [
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('cart',views.cart),
    path('rig',views.rig),
    # path('image',views.image),
]