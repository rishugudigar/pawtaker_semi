from django.urls import path
from . import views
from .views import display,ProfileView,Data,ProfileEditView,ServicePriceView,ServicePriceEditView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'caretaker'

urlpatterns = [
    
    path('display', views.display, name='display'),
    path('', views.index , name="index"),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('forms/',Data.as_view(),name="Data"),
    path('edit/<int:pk>/',ProfileEditView.as_view(), name='profile-edit'),
    path('service_price/', ServicePriceView.as_view(), name='service_price'),
    path('service-price/edit/<int:pk>/', ServicePriceEditView.as_view(), name='service-price-edit'),

]

    
    


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


