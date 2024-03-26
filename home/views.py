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

@login_required(login_url='Player')
def PlayerProfile(request):
   user = request.user
   context = {
               "uname": user.username,
               "email" : user.email,
            }
   return render (request,"PlayerProfile.html",context)


def ChangePass(request):
   return render (request,"ChangePass.html")

def Player(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            
            return redirect('PlayerProfile')
        
        else:
            messages.warning(request, 'Username or Password is incorrect')
            return redirect('Player')
      

        
    return render(request, "Player.html")


def TermsOfService(request):
   return render (request,"TermsOfService.html")

























