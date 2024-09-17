from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from classes.models import Classes
from courses.models import Courses
from teacher.models import Teacher
from classPeriod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import CoursesSerializer
from .serializers import ClassesSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from rest_framework import status

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailview(APIView):
     def put(self,request,id):
       student=Student.objects.get(id=id)
       serializer=StudentSerializer(student,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     def delete(self,request,id):
       student=Student.objects.get(id=id)
       student.delete()
       return Response(status=status.HTTP_202_ACCEPTED)   
   
   
class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
class CoursesDetailview(APIView):
    def put(self,request,id):
       courses=Courses.objects.get(id=id)
       serializer=StudentSerializer(courses,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
       courses=Courses.objects.get(id=id)
       courses.delete()
       return Response(status=status.HTTP_202_ACCEPTED)           

class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer =ClassesSerializer(classes, many=True)
        return Response(serializer.data) 
    def post(self,request):
        serializer=ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
        first_name = request.query_param.get("first_name")
        if first_name:
            student = Student.filter(first_name = first_name)
            serializer= StudentSerializer(student, many= True)
            return request

class ClassesDetailview(APIView):
    def put(self,request,id):
        classes= Classes.objects.get(id=id)
        serializer =ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
       classes=Classes.objects.get(id=id)
       classes.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  

    def enroll(self, student, course_id):
        course = Courses.objects.get(id = course_id)
        student.courses.add(course)   

    def post(self, request, id):
        student = Student.objects.get(id = id)
        action= request.data.get("action")
        if action == "enroll":
           course_id = request.data.get(course_id)
           self.enroll(Student, course_id)
           return Response(status=status.HTTP_201_CREATED)
    

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer =TeacherSerializer(teachers, many=True)
        return Response(serializer.data) 
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailview(APIView):
   def put(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   def delete(self,request,id):
       teachers=Teacher.objects.get(id=id)
       teachers.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  
                 
class ClassperiodListView(APIView):
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer =ClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodDetailview(APIView):
   def put(self,request,id):
        classPeriod= ClassPeriod.objects.get(id=id)
        serializer =TeacherSerializer(classPeriod,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   def delete(self,request,id):
       classPeriod=ClassPeriod.objects.get(id=id)
       classPeriod.delete()
       return Response(status=status.HTTP_202_ACCEPTED)         

                     
    
       

























