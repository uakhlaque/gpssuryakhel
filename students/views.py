from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect
from .forms import StudentSearchForm
import pandas as pd
from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib import messages





# Create your views here.
@login_required


def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all().order_by('student_number')
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


# def add(request):
#   if request.method == 'POST':
#     form = StudentForm(request.POST)
#     if form.is_valid():
#       new_student_number = form.cleaned_data['student_number']
#       new_first_name = form.cleaned_data['first_name']
#       new_last_name = form.cleaned_data['last_name']
#       new_father_name = form.cleaned_data['father_name']
#       new_b_form_no = form.cleaned_data['b_form_no']
#       new_dob = form.cleaned_data['dob']
#       new_age = form.cleaned_data['age']
#       new_class_name = form.cleaned_data['class_name']
#       new_contact = form.cleaned_data['contact']


#       new_student = Student(
#         student_number=new_student_number,
#         first_name=new_first_name,
#         last_name=new_last_name,
#         father_name=new_father_name,
#         b_form_no=new_b_form_no,
#         dob=new_dob,
#         age=new_age,
#         class_name=new_class_name,
#         contact=new_contact,
#       )
  
#       new_student.save()
#       return render(request, 'students/add.html', {
#         'form': StudentForm(),
#         'success': True
#       })
#   else:
#     form = StudentForm()
    
#   return render(request, 'students/add.html', {
#     'form': StudentForm()
#   })

from django.db import IntegrityError

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'students/add.html', {
                  'form': form,
                  'success': True
               })
                # Use the message framework to give feedback to the user
                # messages.success(request, 'Student added successfully!')
                # return redirect('index')
            except IntegrityError:
                messages.error(request, 'This student number and/or B form number already exists.')
        else:
            messages.error(request, 'Error adding student. Please check the form.')
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {'form': form})










def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))




def student_search(request):
    student_number = request.GET.get('student_number', None)
    if student_number:
        students = Student.objects.filter(student_number=student_number)
        if students.exists():
            student = students.first()  # just get the first student if multiple found
            data = {
                'first_name': student.first_name,
                'last_name': student.last_name,
                'father_name': student.father_name,
                'b_form_no': student.b_form_no,
                'dob': student.dob,
                'age': student.age,
                'class_name': student.class_name,
                'contact': student.contact,
            }
        
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Student not found'}, status=404)
    return render(request, 'students/templates/students/index.html')




def export_to_excel(request):
    # This part remains similar to your management command
    students = Student.objects.all().values()
    df = pd.DataFrame.from_records(students)

    # Prepare the response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students_data.xlsx"'

    # Write the dataframe to the response stream
    df.to_excel(response, index=False, engine='openpyxl')

    return response


def import_from_excel(request):
    if request.method == 'POST' and request.FILES['myfile']:
        file = request.FILES['myfile']

        df = pd.read_excel(file, engine='openpyxl')

        for index, row in df.iterrows():
            student_number = row['student_number']
            first_name = row['first_name']
            last_name = row['last_name']
            father_name = row['father_name']
            b_form_no = row['b_form_no']
            dob = row['dob']
            age = row['age']
            class_name = row['class_name']
            contact = row['contact']
            

            student, created = Student.objects.update_or_create(
                student_number=student_number,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'father_name': father_name,
                    'b_form_no': b_form_no,
                    'dob': dob,
                    'age': age,
                    'class_name': class_name,
                    'contact': contact,

                }
            )
            student.save()

        return redirect('index')  # redirect to some page

    return render(request, 'students/import_page.html')  # your import form template





# def import_from_excel(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         file = request.FILES['myfile']

#         df = pd.read_excel(file, engine='openpyxl')
        
#         print(f"Total Rows in Excel: {len(df)}")  # Print total rows in the dataframe

#         for index, row in df.iterrows():
#             try:
#                 print(f"Processing Row: {index}")  # Print the current row index
#                 student_number = row['student_number']
#                 first_name = row['first_name']
#                 last_name = row['last_name']
#                 father_name = row['father_name']
#                 b_form_no = row['b_form_no']
#                 dob = row['dob']
#                 age = row['age']
#                 class_name = row['class_name']
#                 contact = row['contact']

#                 student, created = Student.objects.update_or_create(
#                     student_number=student_number,
#                     defaults={
#                         'first_name': first_name,
#                         'last_name': last_name,
#                         'father_name': father_name,
#                         'b_form_no': b_form_no,
#                         'dob': dob,
#                         'age': age,
#                         'class_name': class_name,
#                         'contact': contact,
#                     }
#                 )
#                 student.save()
#             except IntegrityError:
#                 print(f"Integrity error occurred for student_number: {student_number}")
#             except Exception as e:
#                 print(f"An error occurred for student_number: {student_number}. Error: {str(e)}")

#         return redirect('index')  # redirect to some page

#     return render(request, 'students/import_page.html')  # your import form template



