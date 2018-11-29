from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_clothing(request, article):
    items = article.objects.all()
    context = {
        'items' : items,
        'header' : 'Shirts'
    }

    return render(request, 'index.html', context)

def add_clothing(request, article):
    if request.method == "POST":
        form = article(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = article()
        return render(request, 'add_new.html', {'form': form})

def edit_clothing(request, pk, articleModel, articleForm):
    item = get_object_or_404(articleModel, pk=pk)

    if request.method == "POST":
        form = articleForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = articleForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def delete_clothing(request, pk, model):
    model.objects.filter(id=pk).delete()

    items = model.objects.all()

    context = {
        'items': items
    }

    return render(request, 'index.html', context)



def display_shirts(request):
    return display_clothing(request, Shirts)

def display_pants(request):
    return display_clothing(request, Pants)

def display_shoes(request):
    return display_clothing(request, Shoes)
    


def add_shirts(request):
    return add_clothing(request, ShirtsForm)

def add_pants(request):
    return add_clothing(request, PantsForm)

def add_shoes(request):
    return add_clothing(request, ShoesForm)



def edit_shirts(request,pk):
    return edit_clothing(request, pk, Shirts, ShirtsForm)

def edit_pants(request,pk):
    return edit_clothing(request, pk, Pants, PantsForm)

def edit_shoes(request,pk):
    return edit_clothing(request, pk, Shoes, ShoesForm)


def delete_shirts(request, pk):
    return delete_clothing(request, pk, Shirts)

def delete_pants(request, pk):
    return delete_clothing(request, pk, Pants)

def delete_shoes(request, pk):
    return delete_clothing(request, pk, Shoes)
