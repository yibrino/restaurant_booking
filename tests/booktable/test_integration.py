from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from booktable.models import BookTable
from customers.models import Customer
from tablelist.models import TableList
from customers.models import Customer

from booktable.serializers import BookTableSerializer

class BookTableTests(APITestCase):

    def setUp(self):
        # Create a Customer instance with the provided credentials
        self.customer = Customer.objects.create(
            customer_username="bookrestaurantno1",
            customer_email="bookrestaurantno1@gmail.com",
            customer_password="No123456789@"
        )

        # Create a TableList instance
        self.table = TableList.objects.create(
            table_name="Table 1",
            table_max_guests=44
        )

        # Create a BookTable instance
        self.booktable = BookTable.objects.create(
            table=self.table,
            customer=self.customer,
            booktable_date="2024-07-22",
            booktable_time="19:00",
            booktable_guests=4
        )

        self.list_url = reverse('booktables-list')
        self.create_url = reverse('booktable-create')
        self.retrieve_url = reverse('booktable-retrieve', kwargs={'pk': self.booktable.pk})
        self.update_url = reverse('booktable-update', kwargs={'pk': self.booktable.pk})
        self.delete_url = reverse('booktable-delete', kwargs={'pk': self.booktable.pk})

    def test_list_booktables(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure there is one booking

    def test_create_booktable(self):
        data = {
            'table': self.table.table_name,
            'customer': self.customer.pk,
            'booktable_date': '2024-07-23',
            'booktable_time': '20:00',
            'booktable_guests': 2
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['booktable_date'], '2024-07-23')
        self.assertEqual(response.data['booktable_time'], '20:00')
        self.assertEqual(response.data['booktable_guests'], 2)

    def test_retrieve_booktable(self):
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booktable_date'], '2024-07-22')

    def test_update_booktable(self):
        data = {
            'booktable_date': '2024-07-24',
            'booktable_time': '21:00',
            'booktable_guests': 3
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booktable_date'], '2024-07-24')
        self.assertEqual(response.data['booktable_time'], '21:00')
        self.assertEqual(response.data['booktable_guests'], 3)

    def test_delete_booktable(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(BookTable.objects.filter(pk=self.booktable.pk).exists())

    def test_create_booktable_missing_fields(self):
        data = {
            'table': self.table.pk,
            'customer': self.customer.pk,
            'booktable_date': '2024-07-25'
            # Missing time and guests
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "Missing required fields.")

    def test_create_booktable_table_already_booked(self):
        data = {
            'table': self.table.pk,
            'customer': self.customer.pk,
            'booktable_date': '2024-07-22',
            'booktable_time': '19:00',
            'booktable_guests': 2
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "Table already booked for this date.")

    def test_retrieve_non_existent_booktable(self):
        non_existent_url = reverse('booktable-retrieve', kwargs={'pk': 999})
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Book Table not found')

    def test_update_non_existent_booktable(self):
        non_existent_url = reverse('booktable-update', kwargs={'pk': 999})
        data = {
            'booktable_date': '2024-07-24',
            'booktable_time': '21:00',
            'booktable_guests': 3
        }
        response = self.client.put(non_existent_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Book Table not found')

    def test_delete_non_existent_booktable(self):
        non_existent_url = reverse('booktable-delete', kwargs={'pk': 999})
        response = self.client.delete(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Book Table not found')
