from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile_setup/', views.profile_setup, name='profile_setup'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('mark_attendance/<int:course_id>/', views.mark_attendance, name='mark_attendance'),
    # path('login', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('attendance_list/<int:course_id>/', views.attendance_list, name='attendance_list'),
    path('', views.home, name='home'),
]
