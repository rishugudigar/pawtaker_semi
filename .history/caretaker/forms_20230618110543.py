from django import forms
from .models import UserProfile, Service

class UserProfileForm(forms.ModelForm):
    services_description = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = UserProfile
        fields = ['name', 'image', 'phone_number', 'backup_phonenumber', 'description', 'services_description', 'form_number', 'first_line', 'second_line', 'city', 'state', 'postal_code']
