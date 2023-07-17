from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = UserProfileForm()
    return render(request, 'add_user.html', {'form': form})

def success(request):
    return render(request, 'success.html')
