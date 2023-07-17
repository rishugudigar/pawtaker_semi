from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'aadhar_number', 'phone_number', 'address', 'description']
