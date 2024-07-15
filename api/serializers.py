from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from classes.models import Classes
from courses.models import Courses
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields='_all_'

class  ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields='_all_'
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='_all_'
                     
           