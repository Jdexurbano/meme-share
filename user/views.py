from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exist')
                return redirect('sign_up')
            else:
                new_user = User.objects.create(username = username, first_name = first_name, last_name = last_name, password = password1)
                new_user.save()
                login(request,new_user)
                messages.success(request,'Succesfully created')
                return redirect('home')
        else:
            messages.error(request,'Password do not match')
            return redirect('sign_up')

    return render(request,'user/sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('sign_in')
    return render(request,'user/sign-in.html')

def sign_out(request):
    logout(request)
    return redirect('index')