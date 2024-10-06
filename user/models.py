from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#custom user field
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_link = models.CharField(max_length=300)

    def __str__(self):
        return str(self.user)