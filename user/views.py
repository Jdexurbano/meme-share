from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request,'user/sign-up.html')