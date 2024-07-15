from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from classes.models import Classes
from courses.models import Courses
from teacher.models import Teacher
from .serializers import StudentSerializer
from .serializers import CoursesSerializer
from .serializers import ClassesSerializer
from .serializers import TeacherSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)  

class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer =ClassesSerializer(classes, many=True)
        return Response(serializer.data)  

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer =TeacherSerializer(teachers, many=True)
        return Response(serializer.data)      
        
    

























