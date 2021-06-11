from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Patients, Accomodation, PatFinance
import random

room_types = Accomodation.objects.filter(no_of_beds_left__gt = 0)
payment_methods = (('None', 'Please select an option'),('Net Banking', 'Net Banking'), ('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'))

class NewUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def random_id():
        return str(random.randint(10000, 99999))
    p = random_id()
    patient_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Patient ID', 'default': p}))
    patient_name =  forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Patient Name'}))
    age = forms.IntegerField(widget = forms.NumberInput(attrs = {'placeholder':'Age'}))
    phone_no = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Phone Number'}))
    profession = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Profession'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))
    confirm_Password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password'}))
    room_type = forms.ModelChoiceField(queryset = room_types)

    class Meta:
        model = User
        fields = ("patient_id", "patient_name", "age", "phone_no", "profession", "password", "room_type", "confirm_Password")

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.patient_id = self.cleaned_data['patient_id']
        if commit:
            user.save()
        return user

    def checkpassword(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('confirm_Password')
        if pw1 and pw2 and pw1!=pw2:
            raise forms.ValidationError('Passwords don\'t match')
        return pw2

class EmpLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    employee_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Employee ID'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ("emp_id", "password")

    def save(self, commit = True):
        user = super(EmpLoginForm, self).save(commit = False)
        user.emp_id = self.cleaned_data['emp_id']
        if commit:
            user.save()
        return user

class PatLoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    patient_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Patient ID'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ("patient_id", "password")

    def save(self, commit = True):
        user = super(PatLoginForm, self).save(commit = False)
        user.patient_id = self.cleaned_data['patient_id']
        if commit:
            user.save()
        return user

class PaymentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    patient_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Patient ID'}))
    no_of_days = forms.IntegerField(widget = forms.NumberInput(attrs = {'placeholder':'No. of days stayed'}))
    payment_method = forms.ChoiceField(choices = payment_methods)

    class Meta:
        model = User
        fields = ("patient_id", "no_of_days", "payment_method")

    def save(self, commit = True):
        user = super(PatLoginForm, self).save(commit = False)
        user.patient_id = self.cleaned_data['patient_id']
        if commit:
            user.save()
        return user

    def checkdays(self):
        days = self.cleaned_data.get('no_of_days')
        if (days <= 0):
            raise forms.ValidationError("No. of days is either negative or 0")
        return days
