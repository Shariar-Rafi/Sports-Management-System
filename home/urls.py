from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("",views.index,name = 'home'),
    path("home",views.index,name = 'home'),
    path("PlayerReg",views.PlayerReg,name = 'PlayerReg'),
    path("TermsOfService",views.TermsOfService,name = 'TermsOfService'),
    path("logout",views.LogoutPage,name = 'logout'),
    path("Player",views.Player,name = 'Player'),





]