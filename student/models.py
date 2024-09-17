from django.db import models

from courses.models import Courses

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    course = models.ManyToManyField(Courses)
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

