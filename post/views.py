from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_post(request):
    return render(request,'post/add_post.html')