from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [
    # Employees
    path(
        "employees/new/",
        login_required(views.EmployeeCreateView.as_view()),
        name="employee_new",
    ),
    path(
        "employees/<str:pk>/",
        login_required(views.EmployeeDetailView.as_view()),
        name="employee_detail",
    ),
    path(
        "employees/update/<str:pk>/",
        login_required(views.EmployeeUpdateView.as_view()),
        name="employee_update",
    ),
    path(
        "employees/delete/<str:pk>/",
        login_required(views.EmployeeDeleteView.as_view()),
        name="employee_delete",
    ),
    # Departments
    path(
        "departments/",
        login_required(views.DepartmentListView.as_view()),
        name="department_list",
    ),
    path(
        "departments/new/",
        login_required(views.DepartmentCreateView.as_view()),
        name="department_new",
    ),
    path(
        "departments/<str:pk>/",
        login_required(views.DepartmentDetailView.as_view()),
        name="department_detail",
    ),
    path(
        "departments/update/<str:pk>/",
        login_required(views.DepartmentUpdateView.as_view()),
        name="department_update",
    ),
    path(
        "departments/delete/<str:pk>/",
        login_required(views.DepartmentDeleteView.as_view()),
        name="department_delete",
    ),
    # Designation
    path(
        "designations/",
        login_required(views.DesignationListView.as_view()),
        name="designation_list",
    ),
    path(
        "designations/new/",
        login_required(views.DesignationCreateView.as_view()),
        name="designation_new",
    ),
    path(
        "designations/<str:pk>/",
        login_required(views.DesignationDetailView.as_view()),
        name="designation_detail",
    ),
    path(
        "designations/update/<str:pk>/",
        login_required(views.DesignationUpdateView.as_view()),
        name="designation_update",
    ),
    path(
        "designations/delete/<str:pk>/",
        login_required(views.DesignationDeleteView.as_view()),
        name="designation_delete",
    ),
]
