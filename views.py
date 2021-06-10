from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee, Patients, Accomodation
from django.contrib import messages
from .forms import NewUserForm, EmpLoginForm, PatLoginForm
from django.contrib.auth import login
from django import forms
import re
# Create your views here.

def homepage(request):
    return render(request, 'apollo/welcome.html')

def emploginpage(request):
    if request.method == "POST":
        form = EmpLoginForm(request.POST)
        if form.is_valid():
            emp_id = request.POST.get('employee_id')
            pw = request.POST.get('password')
            if Employee.objects.filter(emp_id=emp_id, password=pw).count() == 1:
                messages.success(request, "Logged in successfully")
                return redirect("apollo:homepage")
        else:
            messages.error(request, "Invalid Login Credentials. Please try again.")
    else:
        form = EmpLoginForm
    return render(request=request, template_name="apollo/emplogin.html", context = {'form':form})


def patregisterpage(request):
    if request.method == "POST":
        input_data = request.POST.dict()
        input_data.pop("csrfmiddlewaretoken", None)
        input_data.pop("confirm_Password", None)
        input_data["room_type"] = Accomodation.objects.get(room_type=input_data["room_type"])
        pat = Patients(**input_data)
        form = NewUserForm(request.POST, instance = pat)
        if form.is_valid():
            user = form.save()
            user.save()
            room = Accomodation.objects.get(room_type=input_data["room_type"])
            room.no_of_beds_left = room.no_of_beds_left - 1
            room.save()
            messages.success(request, "Registration successful!!")
            return redirect("apollo:homepage")
        else:
            print(input_data.values())
            messages.error(request, "Registration unsuccessful. Please make sure you enter valid details, and try again")
            return render(request, "apollo/patregister.html", context = {'form':form})
    else:
        form = NewUserForm
    return render(request, 'apollo/patregister.html', context = {"form":form})

def patloginpage(request):
    if request.method == "POST":
        form = PatLoginForm(request.POST)
        if form.is_valid():
            patient_id = request.POST.get('patient_id')
            pw = request.POST.get('password')
            if Patients.objects.filter(patient_id=patient_id, password=pw).count() == 1:
                messages.success(request, "Logged in successfully")
                return redirect("apollo:homepage")
        else:
            messages.error(request, "Invalid Login Credentials. Please try again.")
    else:
        form = PatLoginForm
    return render(request=request, template_name="apollo/patlogin.html", context = {'form':form})
