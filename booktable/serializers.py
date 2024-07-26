from rest_framework import serializers

from .models import BookTable
class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = ['booktable_id', 'customer','booktable_date','table','booktable_time','booktable_guests','created_at']
    

