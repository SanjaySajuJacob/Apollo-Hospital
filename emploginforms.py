from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    emp_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Employee ID'}))
    emp_name =  forms.CharField(widget = forms.TextInput(attrs = {'placeholder':Employee Name'}))
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ("patient_id", "patient_name", "age", "phone_no", "profession", "password", "room_type", "emp_id", "emp_name")

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.patient_id = self.cleaned_data['patient_id']
        if commit:
            user.save()
        return user
