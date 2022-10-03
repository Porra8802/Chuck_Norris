from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path("home/", views.index, name="home"), #redirecciona al home de mi página
    path("register/", views.register, name="register"), 
    path("profile/", views.profile, name="profile"), 
    path("login/", auth_view.LoginView.as_view(template_name='norrisjokes/login.html'), name='login'),
    path("logout/", auth_view.LogoutView.as_view(template_name='norrisjokes/logout.html'), name='logout'),
    path("jokes/", views.get_jokes, name='jokes'),
]

