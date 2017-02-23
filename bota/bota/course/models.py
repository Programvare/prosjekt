from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    CourseID = models.CharField(max_length=10)
    Name = models.CharField(max_length=20, default='TBA')
    Term = models.CharField(max_length=10, default='TBA')
    Description = models.CharField(max_length=45)

    def __str__(self):
        return self.CourseID


class Takes(models.Model):
    CourseID = models.ForeignKey(Course)
    UserID= models.ForeignKey(User)


class TAin(models.Model):
    CourseID = models.ForeignKey(Course)
    UserID = models.ForeignKey(User)


"""class TATime(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.CharField(max_length=200, help_text="E.g.: <em>hh:mm</em>.")
    end_time = models.CharField(max_length=200, help_text="E.g.: <em>hh:mm</em>.")
    teaching_assistant = models.CharField(max_length=200)
    room = models.CharField(max_length=200)

    def __str__(self):
        return str(self.room) + ": " + str(self.start_time) + "-" + str(self.end_time) + ", " + str(self.date)
"""