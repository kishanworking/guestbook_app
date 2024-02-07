

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views



urlpatterns = [
    
    path('',views.HomePage.as_view() ,name='home'),
    path('signup/', views.SignupPage.as_view() ,name='signup'),
    path('login/',views.LoginPage.as_view() ,name='login'),
    
    path('logout/', login_required(views.LogoutPage.as_view()) , name='logout'),
    
]