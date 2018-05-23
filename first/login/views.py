from django.shortcuts import render
from login.forms import UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'login/index.html')


def signup(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password,user.re_password)
            user.save()
        else:
                

    return render(request,'login/signup.html')

def login(request):
    return render(request,'login/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


