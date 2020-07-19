# from django.http import HttpResponse
# from django.shortcuts import render, redirect


# from employees.forms import SearchName
# from .forms import NameForm

# from django.views.generic import TemplateView

# EMPLOYEES_LIST = [
#     {"name": "camilo", "lastname": "ariza"},
#     {"name": "mafda", "lastname": "apellido"},
#     {"name": "ariza", "lastname": "apellido"},
#     {"name": "rodriguez", "lastname": "apellido"},
# ]


# class employeesList(TemplateView):
#     template_name = "employees_list.html"
#     form = NameForm

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.all_employees = EMPLOYEES_LIST
#         self.current_employees = EMPLOYEES_LIST

#     def post(self, request):
#         def search(string, employee):
#             return string in employee.values()

#         self.current_employees = filter(search, self.all_employees)
#         return redirect("/")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = NameForm
#         context["employees_list"] = self.current_employees
#         return context

from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .forms import EmployeesForm
from .models import Employees


def index(request):
    new_employee_form = EmployeesForm()
    employees = Employees.objects.all()
    return render(
        request,
        "employees_list.html",
        {"new_employee_form": new_employee_form, "employees": employees},
    )


def postEmployees(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = EmployeesForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new Employees object in json
            ser_instance = serializers.serialize("json", [instance])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors ocurred.
            return JsonResponse({"error": form.errors}, status=400)

    # some error ocurred
    return JsonResponse({"error": ""}, status=400)
