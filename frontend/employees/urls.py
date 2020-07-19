from django.urls import path

from . import views

urlpatterns = [
    path("", views.employeeList, name="employees_list"),
    path("search/", views.employeeSearch, name="employee_search"),
    path("post/ajax/employee", views.employeeNew, name="employee_new"),
]
