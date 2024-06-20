from django.shortcuts import render, redirect


def login_user(request):
    return render(request, 'authentication/login.html', {})

def signup_user(request):
    return render(request, 'authentication/signup.html', {})
