from django import forms
from .models import Employees
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.Form):
    search_text = forms.CharField(label=_("Insert text"), max_length=100)


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
        labels = {
            "document": _("Document"),
            "name": _("Name"),
            "lastname": _("Last Name"),
            "salary": _("Salary"),
        }
