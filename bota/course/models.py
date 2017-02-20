from django.db import models

class User(models.Model):
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    Role = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName

class Course(models.Model):
    CourseID = models.CharField(max_length=7)
    Description = models.CharField(max_length=45)

    def __str__(self):
        return self.CourseID

class Takes(models.Model):
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    UserID= models.ForeignKey(User, on_delete=models.CASCADE)