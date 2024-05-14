from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('profile/', views.profile, name='profile'),
    path('routine/', views.routine, name='routine'),
    path('diplomaroutine/', views.DiplomaRoutine, name='diplomaroutine')
]
