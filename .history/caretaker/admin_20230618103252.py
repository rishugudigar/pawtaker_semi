from django.contrib import admin
from .models import UserProfile, Service, ServiceDescription

admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(ServiceDescription)
