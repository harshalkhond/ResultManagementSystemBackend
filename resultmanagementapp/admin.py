from django.contrib import admin
from .models import Result,Task, Token, UserInfo, Students, Subject, Attendance, Grade,Course,Parent,Teacher, Examination, CourseSubject, CourseSubjectMarks, Notice
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Students)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(CourseSubjectMarks)
admin.site.register(CourseSubject)
admin.site.register(Token)
admin.site.register(Notice)
admin.site.register(Task)
admin.site.register(Result)
admin.site.register(Examination)
