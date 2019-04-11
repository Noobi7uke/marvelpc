from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^register$',views.user_register),
    url(r'^login$',views.user_login),
    url(r'^logout$',views.user_logout),
]