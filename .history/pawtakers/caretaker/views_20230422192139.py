from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfileForm()
    return render(request, 'add_user.html', {'form': form})

def success(request):
    return render(request, 'success.html')
