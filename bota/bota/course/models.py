from django.db import models
from django.contrib.auth.models import User
#from bota.account import botaUser as User


class Course(models.Model):
    CourseID = models.CharField(max_length=10,
                                help_text="Use upper case letters followed by 4 numbers: Example: TDT4100")
    Name = models.CharField(max_length=80)
    Nickname = models.CharField(max_length=20, null=True, default="TBA",
                                help_text="Please enter a nickname for the course if possible")
    Term = models.CharField(max_length=20,
                            help_text="Please use the following format: <season> <year>. Example: Spring 2017")
    Description = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.CourseID


class Takes(models.Model):
    CourseID = models.ForeignKey(Course)
    UserID = models.ForeignKey(User)

    def __str__(self):
        return str(self.UserID) + " - " + str(self.CourseID)


class TAin(models.Model):
    CourseID = models.ForeignKey(Course)
    UserID = models.ForeignKey(User)

    def __str__(self):
        return str(self.UserID) + " - " + str(self.CourseID)


class TATime(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    start_time = models.TimeField(help_text="Please use the following format: <em>hh:mm</em>")
    end_time = models.TimeField(help_text="Please use the following format: <em>hh:mm</em>")
    teaching_assistant = models.CharField(max_length=45)
    room = models.CharField(max_length=20)

    def __str__(self):
        return str(self.date) + ": " + str(self.start_time) + "-" + str(self.end_time) + ", " + str(self.room)
