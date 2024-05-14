from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    username = request.user.username

    return render(request, 'index.html', {'username' : username})

def courses(request):
    username = request.user.username

    courses = Curriculam.objects.all()

    return render(request, 'courses.html', {'courses' : courses, 'username' : username})

def teachers(request):
    username = request.user.username

    teachers = Instructor.objects.all()

    return render(request, 'teachers.html', {'teachers' : teachers, 'username' : username})

def students(request):
    username = request.user.username

    students_Hsc = StudentInfo_HSC_Intake.objects.all()
    students_Diploma = StudentInfo_Diploma_Intake.objects.all()

    return render(request, 'students.html', {'studentsHSC' : students_Hsc, 'studentsDiploma' : students_Diploma, 'username' : username})

def profile(request):

    username = request.user.username
    useremail = request.user.email

    return render(request, 'profile.html', {'username' : username, 'email' : useremail})

def routine(request):
    username = request.user.username

    return render(request, 'routine.html', {'username' : username})