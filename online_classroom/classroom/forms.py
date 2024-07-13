from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile, InstructorProfile, Course, Assignment, Submission

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['bio']

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['bio']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor']

class AssignmentForm(forms.ModelForm):
    due_date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%d'],
                                   widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
                                   help_text='Enter a date and time (e.g., YYYY-MM-DD HH:MM:SS)')

    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'due_date', 'max_grade']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['content']
