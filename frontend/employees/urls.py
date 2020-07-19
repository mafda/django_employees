from django.urls import path

from . import views

urlpatterns = [
    path("", views.employeesList.as_view(), name="employees_list"),
]
