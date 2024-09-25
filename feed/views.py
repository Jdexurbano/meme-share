from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'feed/base.html')


def home_page(request):
    return render(request,'feed/home.html')