from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    CourseID = models.CharField(max_length=7)
    Description = models.CharField(max_length=45)

    def __str__(self):
        return self.CourseID

class Takes(models.Model):
    CourseID = models.ForeignKey(Course)
    UserID= models.ForeignKey(User)