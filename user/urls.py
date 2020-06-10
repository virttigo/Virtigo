from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('sponsored', views.sponsored),
    path('', views.home),
    path('blog', views.blog),
    path('contact', views.contact),
    path('earn', views.earn_post),
    
    
    

]