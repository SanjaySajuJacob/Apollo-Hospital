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
        if request.POST.get('Full Name'):
            post = Employee(emp_name=request.POST.get('Full Name'))
    else:
        return render(request, 'apollo/emploginpage.html')

def emploginpage(request):
    if request.method == "POST":
        if request.POST.get('EmpID'):
            post = Employee(emp_id=request.POST.get('EmpID'))
            post.save()
        if request.POST.get('Full Name'):
            post = Employee(emp_name=request.POST.get('Full Name'))
    else:
        return render(request, 'apollo/emploginpage.html')
