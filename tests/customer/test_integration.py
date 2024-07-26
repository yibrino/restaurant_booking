from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from rest_framework import status
from customers.models import Customer
from customers.serializers import CustomerSerializer

class CustomerViewSetTest(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = Client()
        
        # Create a customer for testing
        self.email = 'bookrestaurantno1@gmail.com'
        self.password = 'No123456789@'
        self.customer = Customer.objects.create(
            customer_username='testuser',
            customer_email=self.email,
            customer_password=make_password(self.password)
        )
        
        # Define URLs for API endpoints
        self.list_url = reverse('customers-list')
        self.create_url = reverse('customer-create')  # Adjust according to your URL configuration

          # Adjust according to your URL configuration
        self.detail_url = reverse('customer-detail', kwargs={'pk': self.customer.pk})
    def test_list_customers(self):
        # Send GET request to list endpoint
        response = self.client.get(self.list_url)
        
        # Check response status and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)  # Expect one customer in the list

    def test_retrieve_customer(self):
        # Send GET request to retrieve endpoint
        response = self.client.get(self.detail_url)
        
        # Check response status and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['customer_email'], self.email)

    def test_update_customer(self):
        # Prepare updated data
        updated_data = {
            'customer_username': 'updateduser',
            'customer_email': 'updatedemail@example.com',
            'customer_password': 'NewPassword123!'
        }
        
        # Send PUT request to update endpoint
        response = self.client.put(self.detail_url, updated_data, content_type='application/json')
        
        # Check response status and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['customer_username'], 'updateduser')
        self.assertEqual(response.json()['customer_email'], 'updatedemail@example.com')

  

    def test_create_customer(self):
        # Prepare data to create a new customer
        new_customer_data = {
            'customer_username': 'newuser',
            'customer_email': 'newemail@example.com',
            'customer_password': 'NewPassword123!'
        }
        
        # Send POST request to create endpoint
        response = self.client.post(self.create_url, new_customer_data, content_type='application/json')
        
        # Check response status and content
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['customer_email'], 'newemail@example.com')

    def test_create_customer_with_existing_email(self):
        # Prepare data with an existing email
        existing_email_data = {
            'customer_username': 'anotheruser',
            'customer_email': self.email,  # Use existing email
            'customer_password': 'AnotherPassword123!'
        }
        
        # Send POST request to create endpoint
        response = self.client.post(self.create_url, existing_email_data, content_type='application/json')
        
        # Check response status and content
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['error'], 'A customer with this email already exists.')
