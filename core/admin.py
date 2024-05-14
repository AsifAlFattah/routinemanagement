from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Curriculam)
admin.site.register(Curriculam_Diploma_Intake)
admin.site.register(FullSyllabus)
admin.site.register(FacultyMember)
admin.site.register(AdjunctFaculty_and_GuestTeacher)
admin.site.register(AllocatedRoom)
admin.site.register(LabSlot)
admin.site.register(StudentInfo_HSC_Intake)
admin.site.register(StudentInfo_Diploma_Intake)
admin.site.register(Semester)
admin.site.register(ClassSlot)
admin.site.register(Room_Allocation_to_Diploma_Intake)
admin.site.register(ClassDaysWithSLots_Diploma_Intake)