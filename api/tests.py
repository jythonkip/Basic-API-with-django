from django.test import TestCase
import requests


# Create your tests here.

class TestApiEndpoint(TestCase):
    def setUp(self) :
        return super().setUp()
    
    def test_list_endpoint(self):
        get_response = requests.get('https://api-person-service.onrender.com/api/list/')

        self.assertEqual(get_response.status_code, 200)