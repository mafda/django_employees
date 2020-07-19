from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="employees_list"),
    path("post/ajax/friend", views.postEmployees, name="post_employee"),
]
