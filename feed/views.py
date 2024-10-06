from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'feed/auth.html')

@login_required
def home_page(request):
    return render(request,'feed/home.html')