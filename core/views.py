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


def DiplomaRoutine(request):
    username = request.user.username

    classdays = ClassDaysWithSLots_Diploma_Intake.objects.all()
    classrooms = Room_Allocation_to_Diploma_Intake.objects.all()
    rooms = { }
        
    for allocation in classrooms:
        # Access the related StudentInfo_Diploma_Intake object
        semester_info = allocation.semester
        # Create the key using year and semester
        key = f"{semester_info.year}{semester_info.semester}"
        # Add to the rooms dictionary
        rooms[key] = allocation.room.room_no

    roomno = {
        '1st2nd' : rooms['1st2nd'],
        '2nd1st' : rooms['2nd1st'],
        '2nd2nd' : rooms['2nd2nd'],
        '3rd1st' : rooms['3rd1st'],
        '3rd2nd' : rooms['3rd2nd'],
        '4th1st' : rooms['4th1st'],
        '4th2nd' : rooms['4th2nd']
    }    
    

    return render(request, 'diplomaroutine.html',{'username':username, 'classdays':classdays, 'rooms':roomno})