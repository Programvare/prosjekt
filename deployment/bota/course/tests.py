from django.test import Client
from django.test import TestCase
from .models import Course, TATime, Assignment, TAin, Takes
from django.contrib.auth.models import User
from .queue import *
from .views import *


# Test models.py


class CourseMethodTests(TestCase):
    course_id = "AAA0000"
    name = "name"
    course = Course(course_id=course_id, name=name)

    def test_course_str(self):
        test = str(self.course)
        check = "AAA0000"
        self.assertEqual(test, check)


class TakesMethodTests(TestCase):
    course = Course(course_id="AAA0000", name="name")
    user = User(username='test_user', password='test_password')
    takes = Takes(course=course, user_id=user)

    def test_takes_str(self):
        test = str(self.takes)
        check = "test_user - AAA0000"
        self.assertEqual(test, check)


class TAinMethodTests(TestCase):
    course = Course(course_id="AAA0000", name="name")
    user = User(username='test_user', password='test_password')
    ta_in = TAin(course=course, user_id=user)

    def test_ta_in_str(self):
        test = str(self.ta_in)
        check = "test_user - AAA0000"
        self.assertEqual(test, check)


class TATimeMethodTests(TestCase):
    course = Course(course_id="AAA0000", name="name")
    date = datetime.date(2000, 1, 1)  # Weekday: Saturday
    start_time = datetime.time(0, 1)
    end_time = datetime.time(23, 59)
    ta = 'Test TA'
    room = 'room'
    ta_time = TATime(course=course, date=date, start_time=start_time, end_time=end_time, teaching_assistant=ta,
                     room=room)

    def test_ta_time_str(self):
        test = str(self.ta_time)
        check = "AAA0000: " + str(self.date)
        self.assertEqual(test, check)

    def test_display_weekly(self):
        test = self.ta_time.display_weekly()
        check = "Saturday: 00:01-23:59 in room room"
        self.assertEqual(test, check)

    def test_display_all(self):
        test = self.ta_time.display_all()
        check = "01/01-00: 00:01-23:59 in room room"
        self.assertEqual(test, check)

    def test_display_week_time(self):
        test = self.ta_time.display_week_time()
        check = "Saturday: 00:01-23:59"
        self.assertEqual(test, check)

    def test_display_all_time(self):
        test = self.ta_time.display_all_time()
        check = "01/01-00: 00:01-23:59"
        self.assertEqual(test, check)

    def test_display_room(self):
        test = self.ta_time.display_room()
        check = "Room: room"
        self.assertEqual(test, check)

    def test_display_ta(self):
        test = self.ta_time.display_ta()
        check = "TA: Test TA"
        self.assertEqual(test, check)


class AssignmentMethodTests(TestCase):
    course = Course(course_id="AAA0000", name="name")
    name = 'name'
    description = 'description'
    delivery_deadline = datetime.datetime(2000, 1, 1, 0, 1)
    demo_deadline = datetime.datetime(2000, 1, 1, 23, 59)
    assignment = Assignment(course=course, name=name, description=description, delivery_deadline=delivery_deadline,
                            demo_deadline=demo_deadline)

    def test_assignment_str(self):
        test = str(self.assignment)
        check = "AAA0000 - name: 00:01, 01/01-00"
        self.assertEqual(test, check)

    def test_display_name(self):
        test = self.assignment.display_name()
        check = 'name'
        self.assertEqual(test, check)

    def test_display_delivery_deadline(self):
        test = self.assignment.display_delivery_deadline()
        check = "Delivery deadline: 00:01, 01/01-00"
        self.assertEqual(test, check)

    def test_display_demo_deadline(self):
        test = self.assignment.display_demo_deadline()
        check = "Demonstration deadline: 23:59, 01/01-00"
        self.assertEqual(test, check)

    def test_display_course(self):
        test = self.assignment.display_course()
        check = "AAA0000"
        self.assertEqual(test, check)


# Test queue.py

class QueueTests(TestCase):
    course1 = Course(course_id="AAA0000", name="name1")
    course2 = Course(course_id="BBB1111", name="name2")
    course3 = Course(course_id="CCC2222", name="name3")
    user1 = User(username='test_user1', password='test_password1')
    user2 = User(username='test_user2', password='test_password2')

    def test_add_to_queue(self):
        add_to_queue(self.user1, self.course1.course_id)
        self.assertEqual(get_position(self.user1, self.course1.course_id), 0)
        add_to_queue(self.user2, self.course1.course_id)
        self.assertEqual(get_position(self.user2, self.course1.course_id), 1)

    def test_rm_from_queue(self):
        add_to_queue(self.user1, self.course2.course_id)
        self.assertEqual(get_length(self.course2.course_id), 1)
        rm_from_queue(self.course2.course_id)
        self.assertEqual(get_length(self.course2.course_id), 0)

    def test_get_next(self):
        # user1 in queue for course1
        self.assertEqual(get_next(self.course1.course_id), self.user1)
        # queue for course2 is empty
        self.assertEqual(get_next(self.course2.course_id), "")

    def test_user_in_queue(self):
        # user2 in queue for course1
        self.assertIs(user_in_queue(self.user2, self.course1.course_id), True)
        # queue for course2 is empty
        self.assertIs(user_in_queue(self.user1, self.course2.course_id), False)

    def test_get_position(self):
        # user2 in queue for course1
        self.assertEqual(get_position(self.user2, self.course1.course_id), 1)
        # queue for course3 doesn't yet exist
        self.assertEqual(get_position(self.user1, self.course3.course_id), 0)

    def test_get_length(self):
        # queue for course3 doesn't yet exist
        self.assertEqual(get_length(self.course3.course_id), 0)
        # queue for course1 has 2 users
        self.assertEqual(get_length(self.course1.course_id), 2)


class TestViews(TestCase):
    def setUp(self):
        course = Course.objects.create(course_id="TDT4140", name="Programvareutvikling", nickname="pu",
                                       description="testing", term="spring")

        Assignment.objects.create(course=course, description="testing", name="Oving 1",
                                  delivery_deadline="1990-05-04 22:15", demo_deadline="1990-05-04 22:15")

        # Normal user
        User.objects.create_user(username='course_user', password='4epape?Huf+V')

        # TA user
        ta_user_object = User.objects.create_user(username='course_ta', password='4epape?Huf+V')
        TAin.objects.create(course=course, user_id=ta_user_object)

        # Admin user
        User.objects.create_user(username='course_admin', password='4epape?Huf+V', is_staff='True')

    def test_call_view_denies_anonymous(self):
        """
        Check that all views deny anonymous users and returns a redirect (code 302)
        """

        anon_client = Client()

        # /course/
        request = anon_client.get('/course/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        # course/TDT4140/
        request = anon_client.get('/course/TDT4140/')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        # course/TDT4140/ta
        request = anon_client.get('/course/TDT4140/ta')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        # course/TDT4140/in_queue
        request = anon_client.get('/course/TDT4140/in_queue')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

        # course/TDT4140/rm_queue
        request = anon_client.get('/course/TDT4140/rm_queue')
        self.assertEqual(302, request.status_code)
        self.assertEqual('/login/', request.url[:7])

    def test_get_pages_user(self):
        """
         Checks that all standard-user pages work
        """

        user_client = Client()
        user_client.login(username='course_user', password='4epape?Huf+V')

        # /course/
        request = user_client.get('/course/')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/
        request = user_client.get('/course/TDT4140/')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/ta does not renders ta template
        request = user_client.get('/course/TDT4140/ta')
        self.assertEqual(200, request.status_code)
        self.assertTemplateNotUsed(request, 'course_ta.html')

        # course/TDT4140/in_queue
        request = user_client.get('/course/TDT4140/in_queue')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/rm_queue
        request = user_client.get('/course/TDT4140/rm_queue')
        self.assertEqual(200, request.status_code)

        user_client.logout()

    def test_get_pages_ta(self):
        """
         Checks that ta has access. Note: TA is otherwise standard user
        """
        ta_client = Client()
        ta_client.login(username='course_ta', password='4epape?Huf+V')

        # course/TDT4140/ta, redirects to correct place
        request = ta_client.get('/course/TDT4140/ta')
        self.assertEqual(200, request.status_code)
        self.assertTemplateUsed(request, 'course_ta.html')

        ta_client.logout()

    def test_get_pages_admin(self):
        """
         Checks that all admin-user pages work
        """

        admin_client = Client()

        admin_client.login(username='course_admin', password='4epape?Huf+V')

        # /course/
        request = admin_client.get('/course/')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/
        request = admin_client.get('/course/TDT4140/')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/ta NOTE: admin is not TA
        request = admin_client.get('/course/TDT4140/ta')
        self.assertEqual(200, request.status_code)
        self.assertTemplateNotUsed(request, 'course_ta.html')

        # course/TDT4140/in_queue
        request = admin_client.get('/course/TDT4140/in_queue')
        self.assertEqual(200, request.status_code)

        # course/TDT4140/rm_queue
        request = admin_client.get('/course/TDT4140/rm_queue')
        self.assertEqual(200, request.status_code)

        admin_client.logout()

    def test_call_div_loads_with_referrer(self):
        user_client = Client()
        user_client.login(username='course_user', password='4epape?Huf+V')
        add_to_queue(user_client, 'TDT4140')

        request = user_client.get('/course/course_position/', {}, HTTP_REFERER='/course/TDT4140/')
        self.assertEqual(200, request.status_code)

        ta_client = Client()
        ta_client.login(username='course_ta', password='4epape?Huf+V')

        request = user_client.get('/course/course_next/', {}, HTTP_REFERER='/course/TDT4140/')
        self.assertEqual(200, request.status_code)


class TestViewHelperTATimes(TestCase):
    def setUp(self):
        new_course = Course.objects.create(course_id="AAA0000", name="name")

        date_week = datetime.date.today()
        date_month = date_week + datetime.timedelta(days=20)

        start_time = datetime.time(0, 1)
        end_time = datetime.time(23, 59)
        ta = 'Test TA'
        room = 'room'

        TATime.objects.create(
            course=new_course, date=date_month, start_time=start_time, end_time=end_time, teaching_assistant=ta,
            room=room)

        TATime.objects.create(
            course=new_course, date=date_week, start_time=start_time, end_time=end_time, teaching_assistant=ta,
            room=room)

    def test_get_all_times(self):
        self.assertEqual(get_all_times("Fake_ID").__len__(), 0)
        self.assertEqual(get_all_times("AAA0000").__len__(), 2)

    def test_get_all_times_after_week(self):
        self.assertEqual(get_all_times_after_week("Fake_ID").__len__(), 0)
        self.assertEqual(get_all_times_after_week("AAA0000").__len__(), 1)

    def test_get_week_times(self):
        self.assertEqual(get_week_times("Fake_ID").__len__(), 0)
        self.assertEqual(get_week_times("AAA0000").__len__(), 1)

    def test_check_can_enter(self):
        self.assertEqual(check_can_enter("Fake_ID"), False)
        self.assertEqual(check_can_enter("AAA0000"), True)


class TestViewHelperTakes(TestCase):
    def setUp(self):
        assignments_course = Course.objects.create(course_id="AAA0000", name="name")
        no_assignments_course = Course.objects.create(course_id="BBB0000", name="name")

        name = 'name'
        description = 'description'
        delivery_deadline = datetime.datetime.today()
        demo_deadline = delivery_deadline + datetime.timedelta(days=2)

        assignment1 = Assignment.objects.create(course=assignments_course,
                                                name=name,
                                                description=description,
                                                delivery_deadline=delivery_deadline,
                                                demo_deadline=demo_deadline)
        assignment2 = Assignment.objects.create(course=assignments_course,
                                                name=name,
                                                description=description,
                                                delivery_deadline=delivery_deadline,
                                                demo_deadline=demo_deadline)
        user = User.objects.create(username='test_user', password='test_password')

        Takes.objects.create(course=assignments_course, user_id=user)
        Takes.objects.create(course=no_assignments_course, user_id=user)

    def test_get_all_course_assignments(self):
        self.assertEqual(get_all_course_assignments("BBB0000").__len__(), 0)
        self.assertEqual(get_all_course_assignments("AAA0000").__len__(), 2)
"""
    def test_get_all_student_assignments(self):
        user_client = Client()
        user_client.login(username='test_user', password='test_password')

        request_with_ass = self.client.get('/course/AAA0000/')

        request_no_ass = self.client.get('/course/AAA0000/')

        self.assertEqual(get_all_student_assignments(request_no_ass), 0)
        self.assertEqual(get_all_student_assignments(request_with_ass), 0)
"""

