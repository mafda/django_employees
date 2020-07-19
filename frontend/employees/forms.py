from django import forms
from .models import Employees


class SearchForm(forms.Form):
    search_text = forms.CharField(label="", max_length=100)


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
