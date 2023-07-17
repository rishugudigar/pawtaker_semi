from django import forms
from .models import UserProfile, Service,ServiceDescription

class UserProfileForm(forms.ModelForm):
    services_description = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.instance.user = user

    class Meta:
        model = UserProfile
        exclude = ['id', 'user','view_counter']

class ServicePriceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ServiceDescription
        fields = ['price']


