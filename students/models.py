from django.db import models



# Create your models here.
# class Student(models.Model):
#   student_number = models.PositiveIntegerField(unique=True)
#   first_name = models.CharField(max_length=50)
#   last_name = models.CharField(max_length=50)
#   email = models.EmailField(max_length=100)
#   field_of_study = models.CharField(max_length=50)
#   gpa = models.FloatField()

#   def __str__(self):
#     return f'Student: {self.first_name} {self.last_name}'





class Student(models.Model):
    student_number = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    b_form_no = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    class_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
