from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length = 100, primary_key = True)
    emp_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    def __str__(self):
        return self.emp_id

class Accomodation(models.Model):
    room_type = models.CharField(max_length = 100, primary_key = True)
    no_of_beds_left = models.IntegerField(default = 100)
    cost = models.IntegerField(default = 10000)
    def __str__(self):
        return self.room_type

class Patients(models.Model):
    patient_id = models.CharField(max_length = 100, primary_key = True)
    patient_name = models.CharField(max_length = 100)
    room_type = models.ForeignKey(Accomodation, on_delete = models.CASCADE)
    age = models.IntegerField(default = 0)
    phone_no = models.IntegerField(default = 9999999999)
    profession = models.CharField(max_length = 100)
    def __str__(self):
        return self.patient_id

class EmpFinance(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    salary = models.IntegerField(default = 10000)
    def __str__(self):
        return self.emp_id

class PatFinance(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete = models.CASCADE)
    payment_method = models.CharField(max_length = 100)
    amount_paid = models.IntegerField(default = 0)
    date = models.DateTimeField('payment_date')
    payment_id = models.CharField(max_length = 100)
    def __str__(self):
        return self.patient_id

class Vaccines(models.Model):
    vaccine_name = models.CharField(max_length = 100, primary_key = True)
    vaccine_stock = models.IntegerField(default = 100)
    vaccine_cost = models.IntegerField(default = 1000)
    def __str__(self):
        return self.vaccine_name

class CovApply(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete = models.CASCADE)
    vaccine_name = models.ForeignKey(Vaccines, on_delete = models.CASCADE)
    covid_test_result = models.CharField(max_length = 10)
    def __str__(self):
        return self.patient_id
