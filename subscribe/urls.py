from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('personal', views.personal),
    path('business', views.business),
    path('ultimate', views.ultimate),
    path('premium', views.premium),
    path('confirm', views.confirm),
    path('payment', views.payment),

]