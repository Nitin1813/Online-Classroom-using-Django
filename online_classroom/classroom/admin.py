from django.contrib import admin
from .models import Course, Student, Assignment, InstructorProfile
from django import forms

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(InstructorProfile)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'due_date']
