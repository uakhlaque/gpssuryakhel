from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'father_name', 'b_form_no', 'dob', 'age', 'class_name' , 'contact']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'father_name': 'Father Name',
      'b_form_no': 'B-Form',
      'dob': 'Date of Birth',
      'age':'Age',
      'class_name':'Class',
      'contact':'Contact',
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'father_name': forms.TextInput(attrs={'class': 'form-control'}),
      'b_form_no': forms.TextInput(attrs={'class': 'form-control'}),
      'dob': forms.DateInput(attrs={'class': 'form-control'}, format='%d/%m/%Y'),
      'age': forms.NumberInput(attrs={'class': 'form-control'}),
      'class_name': forms.TextInput(attrs={'class': 'form-control'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control'}),

    }

class StudentSearchForm(forms.Form):
    student_number = forms.CharField(max_length=100, required=False, label="Student Number")