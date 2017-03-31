from django.test import TestCase
from .models import Course, TATime, Assignment, TAin, Takes
from .queue import *
from django.contrib.auth.models import User
import datetime

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

