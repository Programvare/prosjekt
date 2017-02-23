from django.contrib import admin

from .models import Course, TATime, Takes, TAin

admin.site.register(Course)
admin.site.register(TATime)
admin.site.register(Takes)
admin.site.register(TAin)
