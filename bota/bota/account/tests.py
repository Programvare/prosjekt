from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class RequestPageTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='4epape?Huf+V')
        User.objects.create_user(username='testadmin', password='4epape?Huf+V', is_staff='True')

    def test_get_pages_as_anonymous(self):
        """
        Checks that a anonymous user do not have access to pages hes not suppost to
        """
        client = Client()

        request = client.get('/change_password/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/promote_user/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/signup/')
        self.assertEqual(200, request.status_code)

        request = client.get('/logout/')
        self.assertEqual(302, request.status_code)

    def test_getPages_admin(self):
        """
        Checks that all admin pages work
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        request = client.get('/change_password/')
        self.assertEqual(200, request.status_code)

        request = client.get('/promote_user/')
        self.assertEqual(200, request.status_code)

        request = client.get('/login/')
        self.assertEqual(200, request.status_code)

        request = client.get('/signup/')
        self.assertEqual(200, request.status_code)

        request = client.get('/logout/')
        self.assertEqual(302, request.status_code)

    def test_getPages_student(self):
        """
        Checks that a normal user(student) cant accsess what he/she is suppost to
        """
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')

        request = client.get('/change_password/')
        self.assertEqual(200, request.status_code)

        request = client.get('/promote_user/')
        self.assertEqual(302, request.status_code)

        request = client.get('/logout/')
        self.assertEqual(302, request.status_code)

        request = client.get('/login/')
        self.assertEqual(200, request.status_code)

        request = client.get('/signup/')
        self.assertEqual(200, request.status_code)

    def test_signup(self):
        client = Client()
        client.post('/signup/', {'username': 'test', 'password1': 'passord1','password2': 'passord1'})
        self.assertEqual(User.objects.filter(username='test').exists(), True)

        client.post('/signup/', {'username': 'test1', 'password1': 'passord1','password1': 'passord1'})
        self.assertEqual(User.objects.filter(username='test1').exists(), False)

    def test_login(self):
        client = Client()
        client.post('/login/', {'username': 'testuser', 'password':'4epape?Huf+V'})
        self.assertEqual(User.objects.get(username='testuser').is_authenticated, True)

    def test_promote_user(self):
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')
        client.get('/promote_user/testuser')
        self.assertEqual(User.objects.get(username="testuser").is_staff, True)