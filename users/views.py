# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile  

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
    return redirect('profile')  # Redirect to profile page if not POST
