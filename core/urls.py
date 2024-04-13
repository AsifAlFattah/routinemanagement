from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
]
