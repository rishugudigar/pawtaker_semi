from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    form_number = models.CharField(max_length=12,null=True)
    phone_number = models.CharField(max_length=10,null=True)
    backup_phonenumber=models.CharField(max_length=10,null=True)
    first_line = models.CharField(max_length=100,null=True)
    second_line = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=50,null=True)
    postal_code = models.CharField(max_length=20,null=True)
    description = models.TextField(null=True)
    services_description=models.TextField(null=True)
    image = models.ImageField(upload_to='caretaker_images/',null=True,blank='true')
    

    def __str__(self):
        return self.name


