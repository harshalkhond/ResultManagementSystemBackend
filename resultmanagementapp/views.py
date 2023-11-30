from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import Students , Attendance, Parent, Task, Teacher, Course, Grade,Examination, Attendance, CourseSubjectMarks, CourseSubject, Notice
from rest_framework.views import APIView 
from .serializers import CourseSubjectSerializers, CourseSubjectMarksSerializers, StudentSerializers , StudentDataSerializers, AttendanceSerializers, ResultSerializers, TaskSerializer, TeacherSerializers, ParentSerializers, GradeSerializers, CourseSerializers,NoticeseSerializer
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate , login
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class LoginView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self , request):
        data = request.data
        print(data)
        if (request.user.is_authenticated):
            print("hello")
            return Response({'status': 'success',"code":200}, status=200)
        user = authenticate(request,username=data['username'],password=data['password'])
        print(user)
        if (user is not None):
            print("Logged in")
            login(request,user)
            return Response({'status': 'success',"code":200}, status=200)
        else:
            print("Unsuccessful")
            return Response({'status': 'Failed',"code":400}, status=400)


class StudentsView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, *args , **kwargs):
        print(request.user)
        name = self.request.query_params.get('name','')
        rollno = self.request.query_params.get('roll',1)
        print(name)
        print(rollno)
        if (name == '' and rollno != 0):
            name = "unknown"
        if (name=='' and rollno==''):
            name = 'z1'
        if (name=='all()'):
            name=''
        result = Students.objects.filter(Q(Name__contains=name) | Q(RollNo = rollno))
        serializer = StudentSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data,'url':settings.MEDIA_ROOT}, status=200)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDataView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll','')
        result = Students.objects.filter(Q(RollNo = roll)).order_by('RollNo')
        serializer = StudentDataSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = StudentDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetCountView(APIView):
        def get(self, request, *args , **kwargs):
            roll = self.request.query_params.get('roll',0)
            print(roll)
            present = Attendance.objects.filter(Q(present=True) & Q(std_id = roll)).count()
            absent = Attendance.objects.filter(Q(absent=True) & Q(std_id = roll)).count()
            return Response({'status': 'success', "Present": present, "Absent":absent}, status=200)    

class AttendanceView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll',0)
        result = Attendance.objects.all()
        serializer = AttendanceSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = AttendanceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ResultView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll',0)
        result = Examination.objects.filter(Q(std_id = roll))
        serializer = ResultSerializers(result , many=True)
        return Response({"students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = ResultSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class TeacherView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll',0)
        result = Teacher.objects.filter(Q(tr_id=roll))
        serializer = TeacherSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ParentView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll',0)
        result = Parent.objects.filter(Q(pr_id=roll))
        serializer = ParentSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = ParentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GradeView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll','')
        result = Grade.objects.all()
        serializer = GradeSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = GradeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class CourseView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('cid',0)
        print(roll)
        if (roll=="0"):
            result = Course.objects.all()
        else:
            result = Course.objects.filter(Q(c_id=roll))
        serializer = CourseSerializers(result , many=True)
        return Response({'status': 'success', "students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class CourseSubjectView(APIView):
    def get(self, request, *args , **kwargs):
        course = self.request.query_params.get('course',0)
        if (course=="0"):
            result = CourseSubject.objects.all()
        else:
            result = CourseSubject.objects.filter(Q(c_id = course))
        serializer = CourseSubjectSerializers(result , many=True)
        return Response({"students": serializer.data}, status=200)
    
    def post(self, request):
        serializer = CourseSubjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CourseSubjectMarksView(APIView):
    def get(self, request, *args , **kwargs):
        roll = self.request.query_params.get('roll',0)
        result = CourseSubjectMarks.objects.filter(Q(std_id = roll))
        serializer = CourseSubjectMarksSerializers(result , many=True)
        return Response({"students": serializer.data}, status=200)
    
    def post(self, request):
        dt = request.data
        print(dt)
        if (type(dt)==list):
            for i in dt:
                serializer = CourseSubjectMarksSerializers(data=i)
                if serializer.is_valid():
                    serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    

class NoticeView(APIView):
    def get(self, request, *args , **kwargs):
        cid_query = self.request.query_params.get('cid',-1)
        result = Notice.objects.filter(Q(cid = cid_query))
        serializer = NoticeseSerializer(result , many=True)
        return Response({"students": serializer.data}, status=200)
    
    def post(self, request):
        dt = request.data
        serializer = NoticeseSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class TaskView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, *args , **kwargs):
        print(request.user)
        cid_query = self.request.query_params.get('cid',-1)
        result = Task.objects.filter(Q(cid = cid_query))
        serializer = TaskSerializer(result , many=True)
        return Response({"students": serializer.data}, status=200)
    
    def post(self, request):
        dt = request.data
        print(dt)
        serializer = TaskSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"failed"},status=status.HTTP_400_BAD_REQUEST)
        
