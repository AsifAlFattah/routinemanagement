from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Curriculam)
admin.site.register(FullSyllabus)
admin.site.register(FacultyMember)
admin.site.register(AdjunctFaculty_and_GuestTeacher)
admin.site.register(AllocatedRoom)
admin.site.register(LabSlot)
admin.site.register(StudentInfo_BiSemester)
admin.site.register(StudentInfo_TriSemester)