from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Employee, Patients
# Create your views here.

def homepage(request):
    return render(request, 'apollo/welcome.html')

def emploginpage(request):
    if request.method == "POST":
        if request.POST.get('EmpID'):
            post = Employee(emp_id=request.POST.get('EmpID'))
            post.save()
            return render(request, 'apollo/emploginpage.html')
        if request.POST.get('Full Name'):
            post = Employee(emp_name=request.POST.get('Full Name'))
            post.save()
            return render(request, 'apollo/emploginpage.html')
    else:
        return render(request, 'apollo/emploginpage.html')

def patloginpage(request):
    if request.method == "POST":
        if request.POST.get('PatID'):
            post = Employee(emp_id=request.POST.get('PatID'))
            post.save()
            return render(request, 'apollo/patloginpage.html')
        if request.POST.get('Patient Name'):
            post = Employee(emp_name=request.POST.get('Patient Name'))
            post.save()
            return render(request, 'apollo/patloginpage.html')
        if request.POST.get('Age'):
            post = Employee(emp_name=request.POST.get('Age'))
            post.save()
            return render(request, 'apollo/patloginpage.html')
        if request.POST.get('Ph No'):
            post = Employee(emp_name=request.POST.get('Ph No'))
            post.save()
            return render(request, 'apollo/patloginpage.html')
        if request.POST.get('Profession'):
            post = Employee(emp_name=request.POST.get('Profession'))
            post.save()
            return render(request, 'apollo/patloginpage.html')
    else:
        return render(request, 'apollo/patloginpage.html')
