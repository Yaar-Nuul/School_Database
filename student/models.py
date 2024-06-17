from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    department = models.CharField(max_length=50)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
