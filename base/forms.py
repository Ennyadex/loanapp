from typing import Any
from django import forms
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':TextInput(
                attrs={
                    'class':"form-control form-control-lg",
                    'placeholder': 'Username'         
                }
                ),
              'email':EmailInput(
                attrs={
                    'class':"form-control form-control-lg",
                    'placeholder': 'Email'    
                }
                ),
              'password':PasswordInput(
                attrs={
                    'class':"form-control form-control-lg",
                    'placeholder': 'Password1'    
                }
                ),
               'password2':PasswordInput(
                attrs={
                    'class':"form-control form-control-lg",
                    'placeholder': 'Password2'    
                }
                ),
        }
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
        return user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField( )
    password = forms.CharField(widget=forms.PasswordInput)