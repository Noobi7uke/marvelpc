from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('mobile','date_of_birth','profile_pic')
        widgets = {'date_of_birth':forms.SelectDateWidget(years=range(1980,2010))}