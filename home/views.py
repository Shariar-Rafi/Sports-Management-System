from django.shortcuts import render,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here. :(

def index(request):
   return render (request,"index.html")



def LogoutPage(request):
   logout (request)
   return redirect('Player')


def PlayerReg(request):
   return render(request, "PlayerReg.html")


def TermsOfService(request):
   return render (request,"TermsOfService.html")
























