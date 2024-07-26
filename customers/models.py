# customer/models.py

from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Auto-increment field for primary key
    customer_username= models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=255, unique=True, default='default@example.com')  # Make email unique
    customer_password = models.CharField(max_length=128)  # Add password field

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self. customer_email
