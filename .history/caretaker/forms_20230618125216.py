from django import forms
from .models import UserProfile, Service,ServiceDescription,Review

class UserProfileForm(forms.ModelForm):
    services_description = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = UserProfile
        fields = ['name', 'image', 'phone_number', 'backup_phonenumber', 'description', 'services_description', 'form_number', 'first_line', 'second_line', 'city', 'state', 'postal_code']



class ServicePriceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service_name = self.instance.service.name
        self.fields['price'].label = f"Price for {service_name}"

    class Meta:
        model = ServiceDescription
        fields = ['price']
        
