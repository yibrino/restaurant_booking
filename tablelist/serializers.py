from rest_framework import serializers

from .models import TableList
class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableList
        fields = ['table_id', 'table_name','table_max_guests','created_at']
      