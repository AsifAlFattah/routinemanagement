from django.db import models

class Semester(models.Model):

    year = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th')
    ]
    semester = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd')
    ]

    year = models.CharField(max_length=50, choices=year)
    semester = models.CharField(max_length=50, choices=semester)

    def __str__(self):
        return self.year+" Year "+self.semester+" Semester"

class Curriculam(models.Model):
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()
    course_class_time_per_week_in_hours = models.FloatField()
    course_contents = models.TextField()

    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_code

class StudentInfo_Diploma_Intake(models.Model):
    year = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th')
    ]
    semester = [
        ('1st','1st'),
        ('2nd','2nd')
    ]
    

    year = models.CharField(max_length=50, choices=year)
    semester = models.CharField(max_length=50, choices=semester)
    number_of_students = models.IntegerField()

    def __str__(self):
        return self.year+" Year "+self.semester+" Semester "+str(self.number_of_students)+" students"

class Curriculam_Diploma_Intake(models.Model):
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()
    course_class_time_per_week_in_hours = models.FloatField()
    course_contents = models.TextField()

    semester = models.ForeignKey(StudentInfo_Diploma_Intake, on_delete=models.CASCADE, related_name='diplomacourses')

    def __str__(self):
        return self.course_code
    
class FullSyllabus(models.Model):
    syllabus = models.FileField()

class FacultyMember(models.Model):
    designations = [
        ('H','Head'),
        ('P','Professor'),
        ('AP','Assistant Professor'),
        ('SL','Senior Lecturer'),
        ('L','Lecturer')
    ]

    name = models.CharField(max_length=80)
    code_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=50, choices=designations)

    def __str__(self):
        return self.name

class AdjunctFaculty_and_GuestTeacher(models.Model):
    name = models.CharField(max_length=80)
    code_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class AllocatedRoom(models.Model):
    room_no = models.IntegerField()
    max_capacity = models.IntegerField()

    def __str__(self):
        return str(self.room_no)

class LabSlot(models.Model):
    lab_no = models.IntegerField()
    
    def __str__(self):
        return self.lab_no
    
class StudentInfo_HSC_Intake(models.Model):
    year = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th')
    ]
    semester = [
        ('1st','1st'),
        ('2nd','2nd')
    ]
    section = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E'),
    ]

    year = models.CharField(max_length=50, choices=year)
    semester = models.CharField(max_length=50, choices=semester)
    section = models.CharField(max_length=20, choices=section)
    number_of_students = models.IntegerField()

    def __str__(self):
        return self.year+" Year "+self.semester+" Semester "+self.section+" Section "+str(self.number_of_students)+" students"


    
class ClassSlot(models.Model):

    starttime = models.TimeField()
    endtime = models.TimeField()

    def __str__(self):
        return f"{str(self.starttime) + ' to ' + str(self.endtime)}"


class ClassDaysWithSLots_Diploma_Intake(models.Model):

    days = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday')
    ]

    day = models.CharField(max_length=50,choices=days)
    slots = models.ManyToManyField(ClassSlot,related_name='classdayswithslots')

    def __str__(self):
        return self.day


class Room_Allocation_to_Diploma_Intake(models.Model):

    semester = models.ForeignKey(StudentInfo_Diploma_Intake, on_delete=models.CASCADE,  related_name='roomallocations')

    room = models.ForeignKey(AllocatedRoom,on_delete=models.CASCADE, related_name='roomallocations')

    def __str__(self):
        return f"{self.semester}, Room: {self.room}"
    
