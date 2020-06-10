from django.shortcuts import render, redirect
from home.models import Blogpost
from .models import Sponsored, Share
from django.contrib.auth.decorators import login_required
# Create your views here.

@ login_required
def dashboard(request):

    

    return render(request, 'dashboard.html' )

def sponsored(request):
    posts = Sponsored.objects.all()

    user = request.user

    context = {
        'posts':posts,
        'user':user,
        
    }
       
    
    return render(request, 'sponsored.html', context)

def earn_post(request):
    posts = Sponsored.objects.all()
    
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Sponsored.objects.get(id=post_id)
        

        if user in post_obj.shared.all():
            post_obj.shared.remove(user)

        else:
            post_obj.shared.add(user)

        share, created = Share.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if share.value == 'Earn':
                share.value = 'Forfeit'
            else:
                share.value = 'Earn'

        
        
        share.save() 


    return redirect('/user/sponsored')



def home(request):
    blogs = Blogpost.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def blog(request):
    blogs = Blogpost.objects.all()
    
    return render(request, 'blog1.html', {'blogs': blogs})

def contact(request):
    return render(request, 'contact1.html')


