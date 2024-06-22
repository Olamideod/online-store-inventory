from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item, Supplier

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="test@example.com")
        self.item = Item.objects.create(name="Test Item", description="Test Description", price=10.00)
        self.item.suppliers.add(self.supplier)

    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'New Item', 'description': 'New Description', 'price': 20.00, 'supplier_ids': [self.supplier.id]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_supplier(self):
        response = self.client.post('/api/suppliers/', {'name': 'New Supplier', 'contact_info': 'new@example.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_suppliers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
