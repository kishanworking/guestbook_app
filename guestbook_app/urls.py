from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='indexx'),
    path('sign/', views.sign, name='sign'),

]
