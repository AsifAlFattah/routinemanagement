from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    username = request.user.username

    return render(request, 'index.html', {'username' : username})

def courses(request):
    courses = Curriculam.objects.all()

    return render(request, 'courses.html', {'courses' : courses})

def teachers(request):
    faculty = FacultyMember.objects.all()
    guest = AdjunctFaculty_and_GuestTeacher.objects.all()

    return render(request, 'teachers.html', {'faculty' : faculty, 'guest' : guest})

def students(request):
    students = StudentInfo_BiSemester.objects.all()

    return render(request, 'students.html', {'students' : students})

def profile(request):

    username = request.user.username
    useremail = request.user.email

    return render(request, 'profile.html', {'username' : username, 'email' : useremail})