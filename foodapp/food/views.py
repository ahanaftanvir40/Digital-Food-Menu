from django.shortcuts import render
from django.http import HttpResponse
from . models import Item
from django.template import loader
from django.shortcuts import redirect
from .forms import ItemForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout #login is basically session
from django.contrib.auth.decorators import login_required #needs login to view page

# Create your views here.
@login_required(login_url='login')
def index(request):
    item_list = Item.objects.all()
    
    context = {
        'item_list' : item_list,
    }
    return render(request , 'food/index.html' , context)

def item(request):
    return HttpResponse('this is item view')

@login_required(login_url='login')
def detail(request, item_id):
    item = Item.objects.get(pk= item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html',context)

@login_required(login_url='login')
def create_item(request):
    form = ItemForm(request.POST or None)
    context ={
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', context)

@login_required(login_url='login')
def update_item(request , id):
    item = Item.objects.get(id = id)

    form = ItemForm(request.POST or None, instance=item)

    context = {
        'item': item,
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', context)

@login_required(login_url='login')
def delete_item(request,id):
    item = Item.objects.get(id = id)

    context ={
        'item': item
    }

    if request.method == "POST":
        item.delete()
        return redirect ('food:index')
    return render(request, 'food/delete-item.html', context )

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


    return render(request, 'food/login.html')

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

    return render(request, 'food/register.html')