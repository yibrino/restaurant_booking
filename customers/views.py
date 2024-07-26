from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        username = request.data.get('customer_username')
        email = request.data.get('customer_email')
        password = request.data.get('customer_password')

        if not username or not email or not password:
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        if Customer.objects.filter(customer_email=email).exists():
            return Response({"error": "A customer with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        customer = Customer(
            customer_username=username,
            customer_email=email,
            customer_password=make_password(password)
        )

        try:
            customer.save()
            serializer = self.get_serializer(customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
  
        # customer_id = request.data.get('customer')  # Expecting customer_id
        customer_username = request.data.get('customer_username')
        customer_email = request.data.get('customer_email')
        customer_password = request.data.get('customer_password')

        # Validate required fields
        if not customer_username or not customer_email or not customer_password  :
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a table with the same date already exists
        
        serializer = CustomerSerializer(customer, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Book Table not found'}, status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        
        return Response(status=status.HTTP_200_OK)
@csrf_exempt
def login_customer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)

        email = data.get('customer_email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(customer_email=email)
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, customer.customer_password):
            return JsonResponse({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def register_customer(request):
    return render(request, 'auth/register_customer.html')

def login_page(request):
    return render(request, 'auth/login_customer.html')

def book_table_page(request):
    return render(request, 'auth/book_table.html')
