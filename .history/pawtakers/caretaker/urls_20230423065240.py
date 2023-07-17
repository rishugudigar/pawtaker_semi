from django.urls import path
from . import views
from .views import add_user, success

app_name = 'caretaker'

urlpatterns = [
    path('add-user/', add_user, name='add_user'),
    path('success/<int:user_id>/', views.success, name='success')

]


