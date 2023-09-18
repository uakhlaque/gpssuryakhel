from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Delete all Student records from the database'

    def handle(self, *args, **kwargs):
        count = Student.objects.all().count()
        Student.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Student records.'))
