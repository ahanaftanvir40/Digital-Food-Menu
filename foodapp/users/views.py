from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout #login is basically session


# Create your views here.
@login_required(login_url= 'login')
def profile_page(request):
    return render(request, 'users/profile.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        userExist = User.objects.filter(username = username)

        if not userExist.exists():
            messages.error(request, "User doesn't exist")
            return redirect('login')
        user = authenticate(username = username, password = password) #checking

        if user is None: #username pass match
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        else:
            login(request, user)
            return redirect('food:index')


    return render(request, 'users/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username) #checking if user already exists

        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('register')
        else:

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                
                
            )

            user.set_password(password) #for hashing the pass
            user.save()
            messages.info(request, 'Account created successfully')
            return redirect('register')

    return render(request, 'users/register.html')