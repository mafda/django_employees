from django.http import HttpResponse
from django.shortcuts import render, redirect


# from employees.forms import SearchName
from .forms import NameForm

from django.views.generic import TemplateView

from django import template

register = template.Library()


EMPLOYEES_LIST = [
    {"name": "camilo", "lastname": "ariza"},
    {"name": "mafda", "lastname": "apellido"},
    {"name": "ariza", "lastname": "apellido"},
    {"name": "rodriguez", "lastname": "apellido"},
]


class employeesList(TemplateView):
    template_name = "employees_list.html"
    form = NameForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_employees = EMPLOYEES_LIST
        self.current_employees = EMPLOYEES_LIST

    def post(self, request):
        def search(string, employee):
            return string in employee.values()

        self.current_employees = filter(search, self.all_employees)
        return redirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NameForm
        context["employees_list"] = self.current_employees
        return context


# def employees_list(request):

#     employees_list = [
#         {"name": "camilo", "lastname": "ariza"},
#         {"name": "mafda", "lastname": "apellido"},
#         {"name": "ariza", "lastname": "apellido"},
#         {"name": "rodriguez", "lastname": "apellido"},
#     ]

#     return render(
#         request,
#         "employees/employees_list.html",
#         {"form": NameForm, "employees_list": employees_list},
#     )


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return render(request, "employees/list.html", {"employees_list": 0})

#     return HttpResponse("/nope!/")
