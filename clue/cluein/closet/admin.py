from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Shirts, Pants, Shoes)
class ViewAdmin(admin.ModelAdmin):
    pass