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
   if request.method == "POST":
      uname = request.POST.get('uname')
      email = request.POST.get('email')
      pass1 = request.POST.get('pass1')
      pass2 = request.POST.get('pass2')

      if pass1!= pass2:
         messages.warning(request, "Both passwords didn't match, please try again!")
      else:
         my_user = User.objects.create_user(uname,email,pass1)
         my_user.save ()
         return redirect('Player')
   return render(request, "PlayerReg.html")


def TermsOfService(request):
   return render (request,"TermsOfService.html")
























