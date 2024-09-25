# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile  
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


#Functionality for profile
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('create_profile')
    # Render the profile template or handle other logic
    return render(request, 'profile.html', {'profile': profile})


def create_profile(request):
    if request.method == 'POST':
        # Handle profile creation logic here
        # For example, create a profile for the user
        Profile.objects.create(user=request.user)
        messages.success(request, 'Profile created successfully!')
        return redirect('profile')
    return render(request, 'create_profile.html')


#Functionality for profile picture change
@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            try:
                profile = request.user.profile
            except Profile.DoesNotExist:
                # Create a profile if it does not exist
                profile = Profile(user=request.user)
            profile.profile_picture = profile_picture
            profile.save()
            messages.success(request, 'Profile picture updated successfully!')
        else:
            messages.error(request, 'No file uploaded.')
        return redirect('profile')
    return redirect('profile')  



# functionality for the setting 
@login_required
def users_setting(request):
    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = request.user

        # Update firstname,lastname, username and email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if username:
            user.username = username
        if email:
            user.email = email

         # Update password using Django's PasswordChangeForm for validation
        if password:
            form = PasswordChangeForm(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, user)  # Prevents logout after password change
                messages.success(request, 'Password updated successfully!')
            else:
                messages.error(request, 'Error updating password: ' + str(form.errors))
                return redirect('users_setting')

        user.save()

        messages.success(request, 'Settings updated successfully!')
        return redirect('users_setting')
    
    # Render the settings page
    return render(request, 'setting.html', {
        'user': request.user,
    })
