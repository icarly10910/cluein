from django import forms
from .models import *

class ShirtsForm(forms.ModelForm):
    class Meta:
        model = Shirts
        fields = ('type', 'price', 'color', 'size', 'weather')

class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        fields = ('type', 'price', 'color', 'size', 'weather')

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ('type', 'price', 'color', 'size', 'weather')