from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True,
                                help_text="Use upper case letters followed by 4 numbers: Example: TDT4100")
    name = models.CharField(max_length=80)
    nickname = models.CharField(max_length=20, blank=True, default="",
                                help_text="Please enter a nickname for the course if possible")
    term = models.CharField(max_length=20, blank=True,
                            help_text="Please use the following format: <season> <year>. Example: Spring 2017")
    description = models.CharField(max_length=45, blank=True, default="")

    def __str__(self):
        return self.course_id

class Queue(models.Model):
    course_id = models.CharField(max_length=10, unique=True,
                                help_text="Use upper case letters followed by 4 numbers: Example: TDT4100")
    queue = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return str("Course: " + self.course_id + ", Queue: "+ self.queue)

class Takes(models.Model):
    course = models.ForeignKey(Course)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.user_id) + " - " + str(self.course)


class TAin(models.Model):
    course = models.ForeignKey(Course)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.user_id) + " - " + str(self.course)


class TATime(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    start_time = models.TimeField(help_text="Please use the following format: <em>hh:mm</em>")
    end_time = models.TimeField(help_text="Please use the following format: <em>hh:mm</em>")
    teaching_assistant = models.CharField(max_length=45)
    room = models.CharField(max_length=20)

    # Used for admin view
    def __str__(self):
        return str(self.course) + ": " + str(self.date)

    # Used in templates
    def display_weekly(self):
        weekdays = {"0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday",
                    "6": "Saturday"}
        weekday = weekdays[self.date.strftime("%w")]

        return weekday + ": " + self.start_time.strftime("%H:%M") + "-" \
               + self.end_time.strftime("%H:%M") + " in room " + str(self.room)

    def display_all(self):
        return self.date.strftime("%d/%m-%y") + ": " + self.start_time.strftime("%H:%M") + "-" \
               + self.end_time.strftime("%H:%M") + " in room " + str(self.room)

    def display_week_time(self):
        weekdays = {"0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday",
                    "6": "Saturday"}
        weekday = weekdays[self.date.strftime("%w")]

        return weekday + ": " + self.start_time.strftime("%H:%M") + "-" + self.end_time.strftime("%H:%M")

    def display_all_time(self):
        return self.date.strftime("%d/%m-%y") + ": " + self.start_time.strftime("%H:%M") + "-" \
               + self.end_time.strftime("%H:%M")

    def display_room(self):
        return "Room: " + str(self.room)

    def display_ta(self):
        return "TA: " + str(self.teaching_assistant)


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    delivery_deadline = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD hh:mm</em>")
    demo_deadline = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD hh:mm</em>")

    # Used for admin view
    def __str__(self):
        return str(self.course) + " - " + str(self.name) + ": " + self.delivery_deadline.strftime("%H:%M, %d/%m-%y")

    # Used in templates
    def display_name(self):
        return str(self.name)

    def display_delivery_deadline(self):
        return "Delivery deadline: " + self.delivery_deadline.strftime("%H:%M, %d/%m-%y")

    def display_demo_deadline(self):
        return "Demonstration deadline: " + self.demo_deadline.strftime("%H:%M, %d/%m-%y")

    def display_course(self):
        return str(self.course.course_id)

