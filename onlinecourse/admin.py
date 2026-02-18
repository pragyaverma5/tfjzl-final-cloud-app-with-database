from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
