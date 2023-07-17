from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile

def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('caretaker:success', user_id=user.id)
    else:
        form = UserProfileForm()
    return render(request, 'add_user.html', {'form': form})

def success(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user = UserProfile.objects.get(id=user_id)
    return render(request, 'success.html', {'user': user})
