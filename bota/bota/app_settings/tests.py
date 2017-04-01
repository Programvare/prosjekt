from django.test import Client
from django.test import TestCase
from bota.course.models import Course, Assignment


class RequestPageTests(TestCase):
    def setUp(self):
        course = Course.objects.create(course_id="TDT4140", name="Programvare utvikling", nickname="pu",description="testing")
        Assignment.objects.create(course=course, description="testing", name="Øving 1", delivery_deadline="1990-05-04 22:15", demo_deadline="1990-05-04 22:15" )

    def test_get_pages_as_anonymous_access(self):
        client = Client()

        request = client.get('/')
        self.assertEqual(200, request.status_code)

        request = client.get('/login/')
        self.assertEqual(200, request.status_code)

    def test_get_pages_as_anonymous_access_denied(self):
        client = Client()

        request = client.get('/settings/')
        self.assertEqual(302, request.status_code)

        request = client.get('/course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/add_course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/edit')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/rm_course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_ta')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_ta/testuser/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/rm_ta/testuser/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_as/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/rm_as/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/edit_as/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])





