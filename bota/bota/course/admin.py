from django.contrib import admin

from .models import Course, Takes, TAin, TATime, Assignment

admin.site.register(Course)
admin.site.register(Takes)
admin.site.register(TAin)
admin.site.register(TATime)
admin.site.register(Assignment)
