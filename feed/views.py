from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post
# Create your views here.


def index(request):
    return render(request,'feed/auth.html')

@login_required
def home_page(request):
    #get all the data from  the Post,User,Profile
    posts = Post.objects.select_related('user__profile').order_by('-created_at')

    context = {
        'posts':posts
    }
    return render(request,'feed/home.html',context)