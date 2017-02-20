from django.contrib import admin

from .models import Course, User

admin.site.register(Course)
admin.site.register(User)