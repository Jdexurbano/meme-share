from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    caption = models.CharField(max_length=300,blank=True)
    image_link = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #primary key from the user
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return self.caption
