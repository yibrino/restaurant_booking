from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import BookTable
from customers.models import Customer
from tablelist.models import TableList

from .serializers import BookTableSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

class BookTableViewSet(viewsets.ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookTableSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
    # Extract data from request
     table_id = request.data.get('table')   # Expecting table_id
     customer_id = request.data.get('customer')  # Expecting customer_id
     booktable_date = request.data.get('booktable_date')
     booktable_time = request.data.get('booktable_time')
     booktable_guests = request.data.get('booktable_guests')

    # Validate required fields
     if not booktable_date or not booktable_time or not booktable_guests or not table_id or not customer_id:
        return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if a table with the same date already exists
     if BookTable.objects.filter(table=table_id, booktable_date=booktable_date).exists():
        return Response({"error": "Table already booked for this date."}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch the Customer instance
     try:
        customer = Customer.objects.get(pk=customer_id)
     except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch the TableList instance
     try:
        table = TableList.objects.get(pk=table_id)
     except TableList.DoesNotExist:
        return Response({"error": "Table not found."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new BookTable instance
     booktable = BookTable(
        table=table,  # Use the TableList instance
        customer=customer,  # Use the Customer instance
        booktable_date=booktable_date,
        booktable_time=booktable_time,
        booktable_guests=booktable_guests
    )

     try:
        booktable.save()
        serializer = self.get_serializer(booktable)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            booktable= BookTable.objects.get(pk=pk)
        except BookTable.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookTableSerializer(booktable)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    def update(self, request, pk=None):
        try:
            booktable = BookTable.objects.get(pk=pk)
        except BookTable.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)
  
        table_id = request.data.get('table')  # Expecting table_id
        # customer_id = request.data.get('customer')  # Expecting customer_id
        booktable_date = request.data.get('booktable_date')
        booktable_time = request.data.get('booktable_time')
        booktable_guests = request.data.get('booktable_guests')

        # Validate required fields
        if not booktable_date or not booktable_time or not booktable_guests or not table_id :
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a table with the same date already exists
        # if BookTable.objects.filter(table=table_id, booktable_date=booktable_date).exists():
        #     return Response({"error": "Table already booked for this date."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookTableSerializer(booktable, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            booktable = BookTable.objects.get(pk=pk)
        except BookTable.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)
        booktable.delete()
        
        return Response(status=status.HTTP_200_OK)
    
