from django.db import models

class user(models.Model):
    FirstName = models.CharField(max_lenght=45)
    LastName = models.CharField(max_length=45)
    Role = models.CharField(max_length=20)

   def __unicode__(self):
        return "{0} {1} {2} {3}".format(
            self, self.FirstName, self.LastName, self.Role)

class course(models.Model):
    CourseID = models.CharField(max_length=7)
    Description = models.CharField(max_length=45)

   def __unicode__(self):
        return "{0} {1} {2}".format(
            self, self.CourseID, self.Description)

