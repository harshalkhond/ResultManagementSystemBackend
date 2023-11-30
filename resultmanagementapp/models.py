from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=200,default="a",unique=True)
    password = models.CharField(max_length=200,default="a",unique=True)
    designation = models.CharField(max_length=200,default="a",unique=True)
    
    def __str__(self):
        return self.username

class Students(models.Model):
    photo = models.ImageField(upload_to='pics',default="no img")
    Name = models.CharField(max_length=200, default="a")
    Class = models.CharField(max_length=200, default="a")
    RollNo = models.IntegerField(primary_key=True)
    Percentage = models.CharField(max_length=200, default="a")
    Reportsto = models.CharField(max_length=200, default="a")
    email = models.CharField(max_length=200, default="a")
    fname = models.CharField(max_length=200, default="a")
    lname = models.CharField(max_length=200, default="a")
    dob = models.CharField(max_length=200, default="a")
    phone = models.CharField(max_length=200, default="a")
    mobile = models.CharField(max_length=200, default="a")
    p_id = models.IntegerField(unique=True)
    status = models.BooleanField()
    password = models.CharField(max_length=45)
    designation = models.CharField(max_length=45,default="Student")
    present = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)
    c_id = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class Parent(models.Model):
    pr_id = models.IntegerField(primary_key=True)
    email =  models.CharField(max_length=200, default="a")
    fname =  models.CharField(max_length=200, default="a")
    lname =  models.CharField(max_length=200, default="a")
    dob =  models.CharField(max_length=200, default="a")
    phone =  models.CharField(max_length=200, default="a")
    mobile = models.CharField(max_length=200, default="a")
    status =  models.BooleanField()
    password = models.CharField(max_length=45)
    designation = models.CharField(max_length=45,default="Parent")

    def __str__(self):
        return self.fname

class Teacher(models.Model):
    tr_id = models.IntegerField(primary_key=True)
    email =  models.CharField(max_length=200, default="a")
    fname =  models.CharField(max_length=200, default="a")
    lname =  models.CharField(max_length=200, default="a")
    dob =  models.CharField(max_length=200, default="a")
    phone =  models.CharField(max_length=200, default="a")
    mobile = models.CharField(max_length=200, default="a")
    status =  models.BooleanField()
    password = models.CharField(max_length=45)
    designation = models.CharField(max_length=45,default="Teacher")

    def __str__(self):
        return self.fname

class Course(models.Model):
    c_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, default="Course")
    desc = models.CharField(max_length=45, default="Desc")
    grade_id = models.IntegerField(unique=True)
    def __str__(self):
        return self.name

class Grade(models.Model):
    g_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45,default="a")
    desc = models.CharField(max_length=45)
    def __str__(self):
        return self.name


class Result(models.Model):
    exam_id = models.IntegerField()
    name = models.CharField(max_length=45,default="a")
    std_id = models.IntegerField()
    c_id = models.IntegerField()
    marks = models.IntegerField()
    class Meta:
        unique_together = (("std_id", "exam_id"),)
    def __str__(self):
        return self.exam_id+self.std_id
    
class Examination(models.Model):
    exam_id = models.IntegerField()
    name = models.CharField(max_length=45,default="a")
    std_id = models.IntegerField()
    c_id = models.IntegerField()
    marks = models.IntegerField()
    class Meta:
        unique_together = (("std_id", "exam_id"),)
    def __str__(self):
        return str(self.std_id)+self.name
class Attendance(models.Model):
    date = models.DateField()
    std_id = models.IntegerField()
    present = models.BooleanField()
    absent = models.BooleanField()
    remarks = models.CharField(max_length=200,default="Good")


    def __str__(self):
        return self.remarks

class Subject(models.Model):
    RollNo = models.CharField(max_length=200,default="a")
    Sub1 = models.CharField(max_length=200,null=True)
    Sub2 = models.CharField(max_length=200,null=True)
    Sub3 = models.CharField(max_length=200,null=True)
    Sub4 = models.CharField(max_length=200,null=True)
    Sub5 = models.CharField(max_length=200,null=True)
    Sub1marks = models.CharField(max_length=200,null=True)
    Sub2marks = models.CharField(max_length=200,null=True)
    Sub3marks = models.CharField(max_length=200,null=True)
    Sub4marks = models.CharField(max_length=200,null=True)
    Sub5marks = models.CharField(max_length=200,null=True)
    Sub1marksobt = models.CharField(max_length=200,null=True)
    Sub2marksobt = models.CharField(max_length=200,null=True)
    Sub3marksobt = models.CharField(max_length=200,null=True)
    Sub4marksobt = models.CharField(max_length=200,null=True)
    Sub5marksobt = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.RollNo
    
class CourseSubject(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    sub_name = models.CharField(max_length=200)
    c_id = models.IntegerField()

    def __str__(self):
        return self.sub_name
    
class CourseSubjectMarks(models.Model):
    sub_id = models.IntegerField()
    std_id = models.IntegerField()
    sub_name= models.CharField(max_length=200)
    marks = models.IntegerField()
    class Meta:
        unique_together = (("std_id", "sub_name"),)
    def __str__(self):
        return str(self.std_id)+self.sub_name
    

class Token(models.Model):
    access = models.CharField(max_length=1000)
    refresh = models.CharField(max_length=1000)
    
class Notice(models.Model):
    cid = models.IntegerField()
    noticeheadline = models.CharField(max_length=100)
    noticedescrip = models.CharField(max_length=200)
    def __str__(self):
        return self.noticeheadline
    
class Task(models.Model):
    cid = models.IntegerField()
    assignee = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=50)
    duedate = models.DateField()
    def __str__(self):
        return self.description

