from django.contrib import admin
from django.urls import path
from resultmanagementapp.views import CustomAuthToken, StudentsView , StudentDataView, GetCountView,AttendanceView,ResultView,TeacherView,ParentView,GradeView,CourseView,CourseSubjectView,CourseSubjectMarksView,NoticeView,TaskView, LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students',StudentsView.as_view(), name='Student Data'),
    path('students/data',StudentDataView.as_view(), name='Subject wise data'),
    path('Result',ResultView.as_view(), name='Result'),
    path('Count',GetCountView.as_view(), name='Count'),
    path('CSMarks', CourseSubjectMarksView.as_view(), name='CSMarks'),
    path('Courses',CourseView.as_view(), name='Courses'),
    path('teachers',TeacherView.as_view(), name='teachers'),
    path('CSub',CourseSubjectView.as_view(), name='CSub'),
    # path('login',LoginView.as_view(), name='login'),
    path('parents',ParentView.as_view(), name='parents'),
    path('notice',NoticeView.as_view(), name='notice'),
    path('task',TaskView.as_view(), name='task'),
    path('Result',GradeView.as_view(), name='Result'),
    path('Attendance',AttendanceView.as_view(), name='Attendance'),
    path('login',CustomAuthToken.as_view(), name='login')
]