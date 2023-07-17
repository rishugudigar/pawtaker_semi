from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .forms import UserProfileForm,ServicePriceForm
from .models import UserProfile,Service,ServiceDescription

from django.forms import formset_factory




def display(request):
     profiles = UserProfile.objects.all()
     
     selected_city = request.GET.get('city')
     if selected_city:
          profiles = profiles.filter(city=selected_city)
     
     cities = UserProfile.objects.values_list('city', flat=True).distinct()
     
     context = {
          'profiles': profiles,
          'cities': cities,
          'selected_city': selected_city,
     }
     
     return render(request, 'home.html', context)





def index(request):
     user_count = UserProfile.objects.count()
     city_count = UserProfile.objects.values('city').distinct().count()
     state_count = UserProfile.objects.values('state').distinct().count()
     
     context = {
          'user_count': user_count,
          'city_count': city_count,
          'state_count': state_count
     }
     
     return render(request,'index.html',context)


class ProfileView(View):
     def get(self, request, pk, *args, **kwargs):
          profile = UserProfile.objects.get(pk=pk)
          user = profile.user
          service_descriptions = profile.services_description.all()
          
          # Increment the view count
          profile.visits_count = F('visits_count') + 1
          profile.save()
          
          # Get the profiles sorted by visits count in descending order
          profiles = UserProfile.objects.all().order_by('-visits_count')
          
          # Assign the count variable for each profile
          for index, p in enumerate(profiles, start=1):
               p.count = index
          
          context = {
               'user': user,
               'profile': profile,
               'service_descriptions': service_descriptions,
               'profiles': profiles
          }

          return render(request, 'profilepage.html', context)
     

class UserProfileForm(forms.ModelForm):
     class Meta:
          model = UserProfile
          exclude = ['id']
          



class Data(View):
     def get(self, request, *args, **kwargs):
          form = UserProfileForm()
          context = {'form': form}
          return render(request, 'form.html', context)

     def post(self, request, *args, **kwargs):
          form = UserProfileForm(request.POST, request.FILES)
          if form.is_valid():
               new_profile = form.save(commit=False)
               new_profile.user = request.user
               new_profile.save()
               form.save_m2m()  # Save many-to-many relationships
               return redirect('/service_price')
          return render(request, 'form.html', {'form': form})

     def display(request):
          user_profile = UserProfile.objects.get(user=request.user)
          service_descriptions = user_profile.get_service_descriptions()
          context = {'service_descriptions': service_descriptions}
          return render(request, 'display.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = UserProfile
     
     fields = ['name', 'image', 'phone_number', 'backup_phonenumber', 'description', 'services_description', 'form_number', 'first_line', 'second_line', 'city', 'state', 'postal_code']
     template_name = 'profile_edit.html'
     
     
          
     def get_success_url(self):
          pk = self.kwargs['pk']
          return HttpResponseRedirect(reverse_lazy('/profile', kwargs={'pk': pk}))
          
     def test_func(self):
          profile = self.get_object()
          return self.request.user == profile.user
     

class ServicePriceView(View):
     def get(self, request):
          user_profile = UserProfile.objects.get(user=request.user)
          service_descriptions = user_profile.get_service_descriptions()
          forms = []
          for service_description in service_descriptions:
               form = ServicePriceForm(instance=service_description)
               forms.append(form)
          context = {'forms': forms}
          return render(request, 'services.html', context)

     def post(self, request):
          user_profile = UserProfile.objects.get(user=request.user)
          service_descriptions = user_profile.get_service_descriptions()
          forms = []
          for service_description in service_descriptions:
               form = ServicePriceForm(request.POST, instance=service_description)
               if form.is_valid():
                    form.save()
               forms.append(form)
               
          if all(form.is_valid() for form in forms):
               return redirect('/display')
          
          context = {'forms': forms}
          return render(request, 'services.html', context)
     
     
