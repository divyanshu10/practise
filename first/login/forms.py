from django import forms
from django.contrib.auth.models import User
from login.models import RegisterForm

class UserForm(forms.Model):
    password= forms.CharField(widget=forms.PasswordInput())
    re_password= forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('first_name','last_name','email','password','re_password')