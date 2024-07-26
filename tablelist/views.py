from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import TableList
from .serializers import TableListSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

class TableListViewSet(viewsets.ModelViewSet):
    queryset = TableList.objects.all()
    serializer_class = TableListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TableListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        
        table_name = request.data.get('table_name')
        table_max_guests = request.data.get('table_max_guests')
        # print("")

        if not table_name or not table_name:
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        if TableList.objects.filter(table_name=table_name).exists():
            return Response({"error": "A table  already exists."}, status=status.HTTP_400_BAD_REQUEST)

        table = TableList(
            table_name=table_name,
            table_max_guests=table_max_guests,
        )

        try:
            table.save()
            serializer = self.get_serializer(table)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            table= TableList.objects.get(pk=pk)
        except TableList.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TableListSerializer(table)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        try:
            table = TableList.objects.get(pk=pk)
        except TableList.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)
  
        table_name = request.data.get('table_name')
        table_max_guests = request.data.get('table_max_guests')

        # Validate required fields
        if not table_name or not table_max_guests:
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        # if TableList.objects.filter(table_name=table_name).exists():
        #     return Response({"error": "A table  already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TableListSerializer(table, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            table = TableList.objects.get(pk=pk)
        except TableList.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)
        table.delete()
        
        return Response(status=status.HTTP_200_OK)
# @csrf_exempt
# def login_customer(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)

#         email = data.get('customer_email')
#         password = data.get('password')

#         if not email or not password:
#             return JsonResponse({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             customer = Customer.objects.get(customer_email=email)
#         except Customer.DoesNotExist:
#             return JsonResponse({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

#         if check_password(password, customer.customer_password):
#             return JsonResponse({"message": "Login successful"}, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

#     return JsonResponse({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# def register_customer(request):
#     return render(request, 'auth/register_customer.html')

# def login_page(request):
#     return render(request, 'auth/login_customer.html')

# def book_table_page(request):
#     return render(request, 'auth/book_table.html')
