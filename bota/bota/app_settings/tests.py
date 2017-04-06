from django.test import Client
from django.test import TestCase
from bota.course.models import Course, Assignment, TATime, TAin, Takes
from django.contrib.auth.models import User


class RequestPageTests(TestCase):
    def setUp(self):
        course = Course.objects.create(course_id="TDT4140", name="Programvare utvikling", nickname="pu",
                                       description="testing", term="spring")
        Assignment.objects.create(course=course, description="testing", name="Oving 1",
                                  delivery_deadline="1990-05-04 22:15", demo_deadline="1990-05-04 22:15")


        User.objects.create_user(username='testuser', password='4epape?Huf+V')
        User.objects.create_user(username='testadmin', password='4epape?Huf+V', is_staff='True')



    def test_get_pages_as_anonymous_access_denied(self):
        """
        Checks that a anonymous user do not have access to pages hes not suppost to
        """
        client = Client()

        request = client.get('/settings/')
        self.assertEqual(302, request.status_code)

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

        request = client.get('/settings/courses/TDT4140/add_takes')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/edit_ta_time/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/rm_takes/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/add_takes/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

    def test_getPages_admin(self):
        """
        Checks that all admin pages work
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        request = client.get('/settings/')
        self.assertEqual(200, request.status_code)

        request = client.get('/course/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/courses/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/courses/add_course/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/courses/TDT4140/edit')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/TDT4140/add_ta')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/TDT4140/add_ta/testuser/')
        self.assertEqual(302, request.status_code)

        request = client.get('/settings/TDT4140/add_as/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/TDT4140/edit_as/1/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/TDT4140/rm_ta/testuser/')
        self.assertEqual(302, request.status_code)

        request = client.get('/settings/TDT4140/rm_as/1/')
        self.assertEqual(302, request.status_code)

        request = client.get('/settings/courses/TDT4140/rm_course/')
        self.assertEqual(302, request.status_code)


    def test_getPages_user(self):
        """
         Checks that all user pages work
        """
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')

        request = client.get('/settings/')
        self.assertEqual(200, request.status_code)

        request = client.get('/settings/courses/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/add_course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/edit')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_ta')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_ta/testuser/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/add_as/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/edit_as/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/rm_ta/testuser/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/TDT4140/rm_as/1/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        request = client.get('/settings/courses/TDT4140/rm_course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

    def test_add_course(self):
        """
         Checks that add course work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        #checks that the course is created using the view
        client.post('/settings/courses/add_course', {'course_id': 'TDT4145', 'name': 'databaser', 'nickname': 'data',
                                            'term': 'spring', 'description': 'test'})
        course = Course.objects.get(course_id="TDT4145")
        self.assertEqual(course.name,'databaser')
        self.assertEqual(course.nickname, 'data')
        self.assertEqual(course.term, 'spring')
        self.assertEqual(course.description, 'test')

        #Checks that you cant overwrite a course that exsists, or make duplicates
        client.post('/settings/courses/add_course', {'course_id': 'TDT4140', 'name': 'programvare utvikling',
                                                     'nickname': 'pu1', 'term': 'spring 2017', 'description': 'test'})
        course = Course.objects.get(course_id="TDT4140")
        self.assertNotEqual(course.name,'programvare utvikling')
        self.assertNotEqual(course.nickname, 'pu1')
        self.assertNotEqual(course.term, 'spring 2017')
        self.assertNotEqual(course.description, 'test')

    def test_edit_course(self):
        """
         Checks that add course work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # checks that the correct course is eddited
        client.post('/settings/courses/TDT4140/edit', {'course_id': 'TDT4140', 'name': 'programvare utvikling',
                                                       'nickname': 'pu1', 'term': 'spring 2016', 'description': 'test'})
        course = Course.objects.get(course_id="TDT4140")
        self.assertEqual(course.name, 'programvare utvikling')
        self.assertEqual(course.nickname, 'pu1')
        self.assertEqual(course.term, 'spring 2016')
        self.assertEqual(course.description, 'test')

    def test_rm_course(self):
        """
         Checks that remove course work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # Checks that the course is indeed removed
        client.post('/settings/courses/TDT4140/rm_course')
        self.assertEqual(False, Course.objects.filter(course_id='TDT4140').exists())

    def test_add_ta_to_course(self):
        """
         Checks that add TA work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # Checks that a new Ta is added to course
        client.get('/settings/courses/TDT4140/add_ta/testuser/')
        self.assertEqual(True, TAin.objects.filter(course__course_id='TDT4140', user_id__username='testuser').exists())

    def test_rm_ta_from_course(self):
        """
         Checks that remove TA work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # Checks that Ta is removed from course
        client.get('/settings/courses/TDT4140/add_ta/testuser/')
        client.get('/settings/courses/TDT4140/rm_ta/testuser/')
        self.assertEqual(False, TAin.objects.filter(course__course_id='TDT4140', user_id__username='testuser').exists())

        # Checks that you do not get a error for removing none existing entry
        request = client.get('/settings/courses/TDT4140/rm_ta/testuser/')
        self.assertEqual(False, TAin.objects.filter(course__course_id='TDT4140', user_id__username='testuser').exists())
        self.assertEqual(302, request.status_code)
        self.assertEqual('/settings/courses/TDT4140/edit', request.url)

    def test_rm_as(self):
        """
         Checks that remove assignment work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # Checks that assignment is removed from course
        client.get('/settings/courses/TDT4140/rm_as/1/')
        self.assertEqual(False, Assignment.objects.filter(id="1").exists())

        # Checks that you do not get a error for removing none existing entry
        request = client.get('/settings/courses/TDT4140/rm_as/1/')
        self.assertEqual(False, Assignment.objects.filter(id="1").exists())
        self.assertEqual(302, request.status_code)
        self.assertEqual('/settings/courses/TDT4140/edit', request.url)

    def test_add_as(self):
        """
         Checks that add assignment work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')
        client.post('/settings/courses/TDT4140/add_as/', {'description': 'testing', 'name': 'Oving 2',
                                                                 'delivery_deadline': '1990-05-04 22:15',
                                                                 'demo_deadline': '1990-05-04 22:15'})
        self.assertEqual(True, Assignment.objects.filter(name="Oving 2").exists())

    def test_edit_as(self):
        """
         Checks that edit assignment work as its supposed to
        """
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        # checks that the correct course is eddited
        client.post('/settings/courses/TDT4140/edit_as/1/', {'description': 'testing 1', 'name': 'Oving 2',
                                                                 'delivery_deadline': '1991-05-04 22:15',
                                                                 'demo_deadline': '1991-05-04 22:15'})
        assignment = Assignment.objects.get(id="1")
        self.assertEqual(assignment.name, 'Oving 2')
        self.assertEqual(assignment.description, 'testing 1')
        self.assertEqual(assignment.delivery_deadline.year, 1991)
        self.assertEqual(assignment.demo_deadline.year, 1991)

    def test_add_ta_time(self):

        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        client.post('/settings/courses/TDT4140/add_ta_time/', {'date': '1991-05-04', 'start_time': '22:15',
                                                             'end_time': '22:20', 'teaching_assistant': 'Bjarne',
                                                             'room': 'r1'})
        self.assertEqual(True, TATime.objects.filter(teaching_assistant='Bjarne', room='r1').exists())

    def test_edit_ta_time(self):
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        client.post('/settings/courses/TDT4140/add_ta_time/', {'date': '1991-05-04', 'start_time': '22:15',
                                                               'end_time': '22:20', 'teaching_assistant': 'Bjarne',
                                                               'room': 'r1'})

        client.post('/settings/courses/TDT4140/edit_ta_time/1/', {'date': '1991-05-04', 'start_time': '21:15',
                                                             'end_time': '23:20', 'teaching_assistant': 'Finn',
                                                             'room': 'r2'})
        tatime = TATime.objects.get(id='1')
        self.assertEqual(tatime.date.year, 1991)
        self.assertEqual(tatime.start_time.hour, 21)
        self.assertEqual(tatime.end_time.hour, 23)
        self.assertEqual(tatime.teaching_assistant, "Finn")

    def test_rm_ta_time(self):
        client = Client()
        client.login(username='testadmin', password='4epape?Huf+V')

        client.post('/settings/courses/TDT4140/add_ta_time/', {'date': '1991-05-04', 'start_time': '22:15',
                                                               'end_time': '22:20', 'teaching_assistant': 'Bjarne',
                                                               'room': 'r1'})
        self.assertEqual(True, TATime.objects.filter(id='1').exists())
        client.get('/settings/courses/TDT4140/rm_ta_time/1/')
        self.assertEqual(False, TATime.objects.filter(id='1').exists())

        request = client.get('/settings/courses/TDT4140/rm_ta_time/1/')
        self.assertEqual(False, TATime.objects.filter(id='1').exists())
        self.assertEqual(302, request.status_code)
        self.assertEqual('/settings/courses/TDT4140/edit', request.url)

    def test_add_takes(self):
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')

    def test_rm_takes_course(self):
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')
        client.post('/settings/courses/TDT4140/add_takes')
        self.assertEqual(True, Takes.objects.filter(course=Course.objects.get(course_id='TDT4140'), user_id=1).exists())
        request = client.get('/settings/courses/TDT4140/rm_takes/1/')
        self.assertEqual(False, Takes.objects.filter(course=Course.objects.get(course_id='TDT4140'), user_id=1).exists())
        self.assertEqual(302, request.status_code)
        self.assertEqual('/settings/edit_course', request.url)

    def test_add_takes_course(self):
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')
        client.post('/settings/courses/TDT4140/add_takes')
        self.assertEqual(True, Takes.objects.filter(course__course_id='TDT4140', user_id__username='testuser').exists())


    def test_user_list_courses(self):
        client = Client()
        client.login(username='testuser', password='4epape?Huf+V')
