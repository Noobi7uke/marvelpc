from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,unique=True)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='profile',blank=True)

    def __str__(self):
        return self.user.name