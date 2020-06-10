from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('blog/', views.blog),
    
    
    path('contact/', views.contact),
]