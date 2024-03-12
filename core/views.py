from django.shortcuts import render
from .models import Curriculam

# Create your views here.
def index(request):

    courses = Curriculam.objects.all()

    return render(request, 'index.html', {'courses' : courses})

