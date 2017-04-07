from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User


class RequestPageTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='4epape?Huf+V')
        User.objects.create_user(username='testadmin', password='4epape?Huf+V', is_staff='True')

    def test_get_pages_as_anonymous_access(self):
        client = Client()

        request = client.get('/')
        self.assertEqual(200, request.status_code)

        request = client.get('/login/')
        self.assertEqual(200, request.status_code)

    def test_getPages_user(self):
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')

        request = client.get('/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/course', request.url)

    def test_getPages_admin(self):
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        request = client.get('/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/settings', request.url)