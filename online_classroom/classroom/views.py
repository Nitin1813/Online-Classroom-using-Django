from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, StudentProfileForm, InstructorProfileForm, CourseForm, AssignmentForm, SubmissionForm
from .models import StudentProfile, InstructorProfile, Course, Assignment, Submission, Attendance

from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'classroom/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_setup')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_setup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        if 'is_student' in request.POST:
            profile_form = StudentProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                student_profile = profile_form.save(commit=False)
                student_profile.user = request.user
                student_profile.save()
                return redirect('home')
        elif 'is_instructor' in request.POST:
            profile_form = InstructorProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                instructor_profile = profile_form.save(commit=False)
                instructor_profile.user = request.user
                instructor_profile.save()
                return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = StudentProfileForm()  # Default form
    return render(request, 'registration/profile_setup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'classroom/add_course.html', {'form': form})

@login_required
def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'classroom/add_assignment.html', {'form': form})

@login_required
def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = StudentProfile.objects.get(user=request.user)
            submission.save()
            return redirect('assignment_detail', assignment_id=assignment.id)
    else:
        form = SubmissionForm()
    return render(request, 'classroom/submit_assignment.html', {'form': form, 'assignment': assignment})

@login_required
def mark_attendance(request, course_id):
    course = Course.objects.get(id=course_id)
    students = StudentProfile.objects.all()
    if request.method == "POST":
        for student in students:
            present = request.POST.get(f'present_{student.id}', 'off') == 'on'
            Attendance.objects.create(course=course, student=student, date=request.POST['date'], present=present)
        return redirect('attendance_list', course_id=course.id)
    return render(request, 'classroom/mark_attendance.html', {'course': course, 'students': students})



def attendance_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    attendances = Attendance.objects.filter(course=course)
    # Add more logic as needed

    return render(request, 'attendance_list.html', {'course': course, 'attendances': attendances})
