import os
import django
import pandas as pd
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()


class Command(BaseCommand):
    help = 'Description of your command.'

    def add_arguments(self, parser):
        # If you want to add command line arguments
        pass

    def handle(self, *args, **kwargs):
        # The actual logic of the command
        pass

from students.models import Student

# Read the Excel file using pandas
df = pd.read_excel('students_data.xlsx', engine='openpyxl')

# Loop through the dataframe and get data
for index, row in df.iterrows():
    student_number = row['student_number']
    first_name = row['first_name']
    last_name = row['last_name']
    email = row['email']
    field_of_study = row['field_of_study']
    gpa = row['gpa']
    # ... get other fields as needed

    # Create and save the model instance
    instance = Student(student_number=student_number, first_name=first_name, last_name=last_name, email=email, field_of_study=field_of_study,gpa=gpa)
    instance.save()
