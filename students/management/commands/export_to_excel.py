from django.core.management.base import BaseCommand
from students.models import Student
import pandas as pd

class Command(BaseCommand):
    help = 'Export students data to Excel'

    def handle(self, *args, **kwargs):
        # Fetch the data
        students = Student.objects.all().values()

        # Convert the QuerySet to DataFrame
        df = pd.DataFrame.from_records(students)

        # Export to Excel
        output_file_name = 'students_data.xlsx'
        df.to_excel(output_file_name, index=False, engine='openpyxl')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully exported student data to {output_file_name}'))
