from rest_framework import serializers

from .models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_username','customer_email','customer_password','created_at']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password on serialization
        }