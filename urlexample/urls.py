from django.urls import path 

from . import views

urlpatterns = [
    path('', views.profile),
    path('99/', views.profile),
    path('<int:number>/', views.profile),
    path('<slug:article_value>/', views.article),# pass it to views
    
]
