from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello, world. You're at the employees index.")


def employees_list(request):
    return render(request, "employees/employees_list.html", {})
