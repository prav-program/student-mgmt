from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_class', 'admission_date']
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
        }