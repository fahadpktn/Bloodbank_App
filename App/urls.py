from django.urls import path

from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    #path('login',views.Login,name='login'),
    path('display',views.Display,name='display'),
    path('add-donor',views.AddDonor,name='add-donor'),
    path('signup',views.Signup,name='signup'),
    path('logout',views.Logout,name='logout'),
]