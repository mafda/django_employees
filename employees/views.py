from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .forms import EmployeesForm, SearchForm
from .models import Employees


def employeeList(request):
    new_employee_form = EmployeesForm()
    employees = Employees.objects.all()
    return render(
        request,
        "list.html",
        {"new_employee_form": new_employee_form, "employees": employees},
    )


def employeeNew(request):
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


def employeeSearch(request):
    return render(request, "search.html", {"form": SearchForm})


def employeeGet(request):
    if request.is_ajax and request.method == "GET":
        search_text = request.GET.get("search_text", None)
        search_text = search_text.strip().lower()
        data = []
        for employee in Employees.objects.all():
            if search_text in str(employee).lower():
                data.append(employee)

        return JsonResponse(
            {"data": serializers.serialize("json", data)}, status=200
        )

    return JsonResponse({}, status=400)
