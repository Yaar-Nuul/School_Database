from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from classes.models import Classes
from courses.models import Courses
from classPeriod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields="__all__"

class  ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields="__all__"
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"
class  ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields="__all__"


           