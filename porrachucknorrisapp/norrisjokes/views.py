from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm
from django.http import HttpResponse
import requests


def index(request):
    return render(request, 'norrisjokes/home.html')

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Hello, {username}, your account was created successfully')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'norrisjokes/register.html', {'form':form})

def profile(request):
    return render(request, 'norrisjokes/profile.html')

def get_jokes(request):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    # if response==:
    #     const { user, error } = await supabase.auth.api.getUser(
    #     'ACCESS_TOKEN_JWT'
    jokes=response.json()
    print(jokes)
    return render(request, 'norrisjokes/jokes.html', {'jokes':jokes})

