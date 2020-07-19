from django import forms
from .models import Employees


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
