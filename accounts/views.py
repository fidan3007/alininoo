from django.shortcuts import render
from accounts.forms import *
from django.contrib.auth.views import LoginView
from accounts.models import User 
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class Register(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

class Login(LoginView):  
    template_name = 'loginup.html'
    form_class = LoginForm
    success_url = '/'