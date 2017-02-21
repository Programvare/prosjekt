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
    UserID= models.ForeignKey(User)