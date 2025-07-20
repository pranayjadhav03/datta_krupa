# main/models.py

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
     STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ]
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     name = models.CharField(max_length=100)
     email = models.EmailField()
     phone = models.CharField(max_length=15) 
     laptop_model = models.CharField(max_length=100) 
     service_type = models.CharField(max_length=100) 
     problem_description = models.TextField() 
     issue_type = models.CharField(max_length=200, blank=True)
     preferred_date = models.DateField()
     message = models.TextField(blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
     
     def __str__(self):
        return self.name


class RefurbishedLaptop(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
