from django.shortcuts import render, redirect
from .models import Blogpost
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    blogs = Blogpost.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def about(request):
    return render(request, 'about.html')


def blog(request):
  
    blogs = Blogpost.objects.all()
    
    return render(request, 'blog.html', {'blogs': blogs})






def contact(request):
    return render(request, 'contact.html')



