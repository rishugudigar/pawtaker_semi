from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    description = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


