from django.test import TestCase, Client

class InventorylTestCase(TestCase):
    def test_get_catagories_for_store(self):
        c = Client()
        response = c.get('/items/pc/')
        assert response.status_code == 200
