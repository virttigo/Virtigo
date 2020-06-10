from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from user.models import UserProfile
from django.contrib import messages
from .forms import UserProfileform

# Create your views here.
def subscribe(request):
    return render(request, 'subscribe.html')

def personal(request):
    form = UserProfileform()
    context = {
        'form' : form
    }
    return render(request, 'personal.html', context)

def business(request):
    form = UserProfileform()
    context = {
        'form' : form
    }
    return render(request, 'business.html', context)

def ultimate(request):
    form = UserProfileform()
    context = {
        'form' : form
    }
    return render(request, 'ultimate.html', context)

def premium(request):
    form = UserProfileform()
    context = {
        'form' : form
    }
    return render(request, 'premium.html', context)

def confirm(request):
    return render(request, 'confirm.html')


def payment(request):
    return render(request, 'payment.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile_form = UserProfileform(request.POST)
        
        

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "UserName already exists !!!")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists !!!")
            else:
                user = User.objects.create_user( first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                if profile_form.is_valid():
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()
                
    
                return redirect('/subscribe/confirm')
        else:
            messages.info(request, "Password Not Matching")
            
        return redirect('/subscribe/register')
        

        
    else:
        form = UserProfileform()
        context = {
            'form' : form
        }
        return render(request, 'register.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        
        if user is not None:
            auth.login(request, user)
            return redirect ('/user')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/subscribe/login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')






