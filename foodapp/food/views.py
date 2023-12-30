from django.shortcuts import render
from django.http import HttpResponse
from . models import Item
from django.template import loader
from django.shortcuts import redirect
from .forms import ItemForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin #login req for class based

from django.contrib.auth.decorators import login_required #needs login to view page

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    
    context = {
        'item_list' : item_list,
    }
    return render(request , 'food/index.html' , context)

# implementing class based view for index

class IndexClassView(LoginRequiredMixin ,ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('this is item view')

#@login_required(login_url='login')
def detail(request, item_id):
    item = Item.objects.get(pk= item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html',context)
# class based for details
class DetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

#@login_required(login_url='login')
def create_item(request):
    form = ItemForm(request.POST or None)
    context ={
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', context)

#class based fro create item
class CreateItem(LoginRequiredMixin,CreateView):
    model = Item
    fields =['item_name','item_desc','item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    




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











