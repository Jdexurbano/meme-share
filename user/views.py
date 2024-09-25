from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']

        new_user = User.objects.create(username = username,first_name = first_name,last_name = last_name, password = password)
        new_user.save()
        login(request,new_user)
        return redirect('home')

    return render(request,'user/sign-up.html')

def sign_in(request):
    return render(request,'user/sign-in.html')