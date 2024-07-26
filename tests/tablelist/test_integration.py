from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tablelist.models import TableList

class TableListTests(APITestCase):
    
    def setUp(self):
        # Create a TableList instance for testing
        self.table = TableList.objects.create(
            table_name="Table 1",
            table_max_guests=4
        )
        
        # URLs for CRUD operations
        self.list_url = reverse('tables-list')
        self.create_url = reverse('table-create')
        self.retrieve_url = reverse('table-retrieve', kwargs={'pk': self.table.pk})
        self.update_url = reverse('booktable-update', kwargs={'pk': self.table.pk})
        self.delete_url = reverse('booktable-delete', kwargs={'pk': self.table.pk})

    def test_list_tables(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure there is one table

    def test_create_table(self):
        data = {
            'table_name': 'Table 2',
            'table_max_guests': 6
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['table_name'], 'Table 2')
        self.assertEqual(response.data['table_max_guests'], 6)

    def test_retrieve_table(self):
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['table_name'], 'Table 1')

    def test_update_table(self):
        data = {
            'table_name': 'Updated Table',
            'table_max_guests': 8
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['table_name'], 'Updated Table')
        self.assertEqual(response.data['table_max_guests'], 8)

    def test_delete_table(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(TableList.objects.filter(pk=self.table.pk).exists())

    def test_create_table_missing_fields(self):
        data = {
            'table_name': 'Table 3'
            # Missing table_max_guests
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "Missing required fields.")

    def test_create_table_duplicate_name(self):
        data = {
            'table_name': 'Table 1',
            'table_max_guests': 4
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "A table already exists.")

    def test_retrieve_non_existent_table(self):
        non_existent_url = reverse('table-retrieve', kwargs={'pk': 999})
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Customer not found')  # Update this error message in views if needed

    def test_update_non_existent_table(self):
        non_existent_url = reverse('booktable-update', kwargs={'pk': 999})
        data = {
            'table_name': 'New Name',
            'table_max_guests': 10
        }
        response = self.client.put(non_existent_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Book Table not found')  # Update this error message in views if needed

    def test_delete_non_existent_table(self):
        non_existent_url = reverse('booktable-delete', kwargs={'pk': 999})
        response = self.client.delete(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Book Table not found')  # Update this error message in views if needed
