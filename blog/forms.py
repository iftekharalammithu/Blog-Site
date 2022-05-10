from cProfile import label
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from turtle import textinput
from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from .models import post1

class signupform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Comfirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username':'User Name', 'first_name':'First Name', 'last_name': 'Last Name', 'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'})
        }

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class postForm(forms.ModelForm):
    class Meta:
        model = post1
        fields = ["title", "desc"]
        lebels = {'title': "Title", "desc": 'Descriptions'}
        widgets={'title':forms.TextInput (attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}