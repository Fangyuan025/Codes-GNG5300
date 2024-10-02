from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not 1 <= grade <= 12:
            raise forms.ValidationError('Grade must be between 1 and 12.')
        return grade