from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@email.se', password='top_secret')

    def test_create_account(self):
        """
        Ensure we can create a new bill object.
        """
        url = reverse('bill-list')
        data = {'amount': 12, 'description': 'yolo'}
        response_data = {'url': 'http://testserver/api/bills/1/', 'owner': 'jacob', 'amount': 12, 'description': 'yolo'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, response_data)
