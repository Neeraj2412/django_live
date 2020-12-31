from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'First Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Email'})
        }


class profileForm(forms.ModelForm):
    phone = forms.CharField()
    phone.widget.attrs.update({'class': 'form-control', 'type': 'mobile', 'placeholder': 'Phone'})
    address = forms.CharField()
    address.widget.attrs.update({'class': 'form-control', 'type': 'textarea', 'placeholder': 'Address'})

    class Meta:
        model = userProfiles
        fields = ['phone', 'address']


# SellerForm

class CreateSellerForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Organisation Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Company Email'})
        }

class sellerProfileForm(forms.ModelForm):
    phoneSeller = forms.CharField()
    phoneSeller.widget.attrs.update({'class': 'form-control', 'type': 'mobile', 'placeholder': 'Org.Phone'})
    addressSeller = forms.CharField()
    addressSeller.widget.attrs.update({'class': 'form-control', 'type': 'textarea', 'placeholder': 'Org. Address'})

    class Meta:
        model = sellerProfile
        fields = ['phoneSeller','addressSeller']
   
