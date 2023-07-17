from django.urls import path
from . import views
from .views import add_user, success

app_name = 'caretaker'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-user/', add_user, name='add_user'),
    path('success/', success, name='success'),
]
