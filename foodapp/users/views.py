from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Register_Form


# Create your views here.

def user_reg(request):

    if request.method == 'POST':
        form = Register_Form(request.POST)
        
        if form.is_valid():
            form.save() #to save the form
            username = form.cleaned_data.get('username') #getting the username
            messages.success(request,f'Welcome {username}! your account is created successfully')
            return redirect('food:index')
    
    else:    
        form = Register_Form()
    context = {
        'form': form
    }
    return render(request, 'users/reg.html', context)