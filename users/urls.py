from . import views
from django.urls import path


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('profile', views.profileuser, name='profile'),
]
