from rest_framework import serializers
from .models import Students , Subject, Parent, Task, Teacher, Course, Grade, Result,Examination, Attendance, CourseSubject, CourseSubjectMarks, Token,  Notice
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class StudentSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Students
        fields = ('photo','image_url','Name', 'Class', 'RollNo', 'Percentage', 'Reportsto','email', 'fname','lname','dob','phone','mobile','p_id','status','password','designation','present','absent','c_id')
        
    def get_image_url(self, obj):
        return obj.photo.url

class StudentDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('RollNo', 'Sub1', 'Sub2', 'Sub3', 'Sub4','Sub5', 'Sub1marks','Sub2marks', 'Sub3marks', 'Sub4marks', 'Sub5marks','Sub1marksobt','Sub2marksobt','Sub3marksobt','Sub4marksobt','Sub5marksobt')

class ParentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('pr_id','email','fname','lname','dob','phone','mobile','status','password','designation')

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('tr_id','email','fname','lname','dob','phone','mobile','status','password','designation')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('c_id','name','desc','grade_id')

class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('g_id','name','desc')

class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ('exam_id','name','std_id','c_id','marks')

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('date','std_id','present','absent','remarks')

class CourseSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseSubject
        fields = ('sub_id','sub_name','c_id')
    
class CourseSubjectMarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseSubjectMarks
        fields = ('sub_id','std_id','marks','sub_name')

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('access','refresh')

class NoticeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('cid','noticeheadline','noticedescrip')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('cid','assignee','description','status','duedate')

class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  ("username","password")
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user