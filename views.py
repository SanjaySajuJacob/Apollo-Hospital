from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Employee, Patients, Accomodation
# Create your views here.

def homepage(request):
    return render(request, 'apollo/welcome.html')

def emploginpage(request):
    if request.method == "POST":
        if request.POST.get('EmpID') and request.POST.get('Full Name') and request.POST.get('Designation') and request.POST.get('Department'):
            post = Employee()
            post.emp_id = request.POST.get('EmpID')
            post.emp_name = request.POST.get('Full Name')
            post.designation = request.POST.get('Designation')
            post.department = request.POST.get('Department')
            post.save()
            return render(request, 'apollo/emplogin.html')
    else:
        return render(request, 'apollo/emplogin.html')

def patloginpage(request):
    if request.method == "POST":
        if request.POST.get('PatID') and request.POST.get('Patient Name') and request.POST.get('Age') and request.POST.get('Ph No') and request.POST.get('Profession'):
            post = Patients()
            post.patient_id = request.POST.get('PatID')
            post.patient_name = request.POST.get('Patient Name')
            post.age = request.POST.get('Age')
            post.phone_no = request.POST.get('Ph No')
            post.profession = request.POST.get('Profession')
            post.room_type = Accomodation(request.POST.get('Room'))
            post.save()
            return render(request, 'apollo/patlogin.html')
    else:
        return render(request, 'apollo/patlogin.html')
