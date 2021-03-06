from django.contrib import admin
from django.db import models
from .models import Accomodation, CovApply, EmpFinance, Employee, PatFinance, Patients, Vaccines
# Register your models here.
class AccomodationAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['room_type', 'no_of_beds_left', 'cost']})]

class CovApplyAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['patient_id', 'vaccine_name', 'covid_test_result']})]

class EmpFinanceAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['emp_id', 'salary']})]

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['emp_id', 'emp_name', 'designation', 'department']})]

class PatFinanceAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['patient_id', 'payment_method', 'amount_paid', 'date']})]

class PatientsAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['patient_id', 'patient_name', 'room_type', 'age', 'phone_no', 'profession']})]

class VaccinesAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['vaccine_name', 'vaccine_stock', 'vaccine_cost']})]

admin.site.register(Accomodation, AccomodationAdmin)
admin.site.register(CovApply, CovApplyAdmin)
admin.site.register(EmpFinance, EmpFinanceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PatFinance, PatFinanceAdmin)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(Vaccines, VaccinesAdmin)
