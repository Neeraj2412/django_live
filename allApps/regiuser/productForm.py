from django.forms import ModelForm, fields
from django import forms

from .models import *

class herbProductForm(forms.ModelForm):
    productName = forms.CharField()
    productName.widget.attrs.update({'class': 'form-control', 'type': 'textarea', 'placeholder': 'Product Name'})
    productPrice = forms.FloatField()
    productPrice.widget.attrs.update({'class': 'form-control', 'type': 'textarea', 'placeholder': 'Price'})
    productDesc = forms.CharField()
    productDesc.widget.attrs.update({'class': 'form-control', 'type': 'textarea', 'placeholder': 'Product Description'})

    class Meta:
        model = herbProduct
        fields = ['productName','productPrice','productDesc','productImage']
