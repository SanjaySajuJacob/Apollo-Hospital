from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee, Patients, Accomodation, PatFinance, Leave
from django.contrib import messages
from .forms import NewUserForm, EmpLoginForm, PatLoginForm, PaymentForm, CovidCare, LeaveForm, ContactForm
from django.contrib.auth import login
from django import forms
from django.utils import timezone
from django.core.mail import send_mail
import random
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
                return redirect("apollo:emphomepage")
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
            return redirect("apollo:pathomepage")
        else:
            formnotvalid = True
            message = "Registration unsuccessful. Please make sure you enter valid details, and try again"
            messages.error(request, "Registration unsuccessful. Please make sure you enter valid details, and try again")
            return render(request, "apollo/patregister.html", context = {'form':form, 'check':formnotvalid, 'message':message})
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
                return redirect("apollo:pathomepage")
        else:
            messages.error(request, "Invalid Login Credentials. Please try again.")
    else:
        form = PatLoginForm
    return render(request=request, template_name="apollo/patlogin.html", context = {'form':form})

def paymentpage(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            paid = True
            patient_id = Patients.objects.get(patient_id=request.POST.get('patient_id'))
            room = Patients.objects.values('room_type').filter(patient_id=patient_id)
            days = request.POST.get('no_of_days')
            accomodate = Accomodation.objects.get(room_type = room[0]["room_type"])
            patfin = PatFinance()
            patfin.amount_paid = int(days)*int((accomodate.cost))
            patfin.patient_id = patient_id
            patfin.payment_method = request.POST.get('payment_method')
            patfin.date = timezone.now()
            patfin.payment_id = random.randint(1000, 9999)
            patfin.save()
            message = "The total cost and your Payment ID are as shown. Kindly go to the payment counter to make your payment. Thank you."
            return render(request, 'apollo/payment.html', context = {'paid':paid, 'message':message, 'cost':patfin.amount_paid, 'payment_id':patfin.payment_id, 'form':form})
        else:
            messages.error(request, "Something went wrong. Please try again")
    else:
        form = PaymentForm
        return render(request, 'apollo/payment.html', context = {'form':form})

def covidcare(request):
    if request.method == "POST":
        form = CovidCare(request.POST)
        if form.is_valid() and Patients.objects.filter(patient_id=request.POST.get('patient_id')).exists():
            patient_id = request.POST.get('patient_id')
            vaccine_name = request.POST.get('vaccine_name')
            covid_test_result = request.POST.get('covid_test_result')
            if CovApply.objects.filter(patient_id=patient_id).count() == 1:
                user = form.save()
                user.save()
                messages.success(request, "Application was successful")
                return redirect("apollo/pathomepage.html")
            else:
                messages.error("Patient already registered")
                return render(request, 'apollo/payment.html', context = {'form':form})
        else:
            messages.error(request, "Please enter valid details")
            return render(request, "apollo/covidcare.html", context = {'form':form})
    else:
        form = CovidCare
    return render(request, "apollo/covidcare.html", context = {'form':form})

def pathomepage(request):
    return render(request, 'apollo/pathomepage.html')

def emphomepage(request):
    return render(request, 'apollo/emphomepage.html')

def leavepage(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid() and Employee.objects.filter(emp_id=request.POST.get('emp_id')).exists():
            leave = Leave()
            leave.emp_id = Employee.objects.get(emp_id=request.POST.get('emp_id'))
            leave.start_date = request.POST.get('start_date')
            leave.end_date = request.POST.get('end_date')
            leave.reason_for_leave = request.POST.get('reason_for_leave')
            leave.save()
            return render(request, 'apollo/pathomepage.html', context = {'form':form, 'approved':'True', 'message':'Your leave has been granted'})
        else:
            return render(request, 'apollo/leavepage.html', context = {'form':form, 'not_approved':'True','message':'Please enter valid details.'})
    else:
        form = LeaveForm
    return render(request, 'apollo/leavepage.html', context = {'form':form})

def contactus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email_id')
            content = request.POST.get('content')
            send_mail("Mail from Hospital", content, email, ['jayanand.jayan2020@vitstudent.ac.in'])
            message = "Your mail has been sent! We will try to get in touch with you as soon as possible."
            sent = True
            return render(request, 'apollo/contactus.html', context = {'form':form, 'message':message, 'sent':sent})
        else:
            notsent = True
            message = "Looks like there was an error in filling the form. Please retry."
            return render(request, 'apollo/contactus.html', context = {'form':form, 'message':message, 'notsent':notsent})
    else:
        form = ContactForm
        return render(request, 'apollo/contactus.html', context = {'form':form})
