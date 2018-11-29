from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_shirts(request):
    items = Shirts.objects.all()
    context = {
        'items' : items,
        'header' : 'Shirts'
    }

    return render(request, 'index.html', context)

def display_pants(request):
    items = Pants.objects.all()
    context = {
        'items' : items,
        'header' : 'Pants',
    }

    return render(request, 'index.html', context)

def display_shoes(request):
    items = Shoes.objects.all()
    context = {
        'items' : items,
        'header' : 'Shoes',
    }

    return render(request, 'index.html', context)

def add_clothing(request, clas):
    if request.method == "POST":
        form = clas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = clas()
        return render(request, 'add_new.html', {'form': form})

def add_shirts(request):
    return add_clothing(request, ShirtsForm)

def add_pants(request):
    return add_clothing(request, PantsForm)

def add_shoes(request):
    return add_clothing(request, ShoesForm)

# def add_pants(request):
#     if request.method == "POST":
#         form = PantsForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = PantsForm()
#         return render(request, 'add_new.html', {'form': form})

# def add_shoes(request):
#     if request.method == "POST":
#         form = ShoesForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ShoesForm()
#         return render(request, 'add_new.html', {'form': form})
