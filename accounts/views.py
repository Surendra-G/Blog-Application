from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Adding backend for registering the new user
def signup_user(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email-address")
        password = request.POST.get("password")
        confirm_password = request.POST.get("Confirmpassword")
        if confirm_password == password:
            if not User.objects.filter(username=email).exists():
                try:
                    user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
                    user.save()
                    messages.success(request, "Account created successfully!")
                    return redirect("login")
                except Exception as e:
                    messages.error(request, f"Error creating account: {e}")
            else:
                messages.error(request, "This email is already in use!")
        else:
            messages.error(request, "Passwords do not match!")
    return render(request, 'authentication/signup.html', {})


# Adding functionality for the login
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'authentication/login.html', {})


# Functionality for the logout process
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("home")
