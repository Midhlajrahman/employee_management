from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from employees.forms import (
    DepartmentForm,
    DesignationForm,
    EmployeeCreateForm,
    EmployeeForm,
)
from employees.models import Department, Designation, Employee
from employees.tables import DepartmentTable, DesignationTable, EmployeeTable

from .models import Employee


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "main/employees/object_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Details"
        context["table"] = EmployeeTable([self.object])
        return context


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "main/common/object_form.html"
    form_class = EmployeeCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy("main:index")


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "main/common/object_form.html"
    form_class = EmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Employee"
        return context

    success_url = reverse_lazy("main:index")


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "main/common/confirm_delete.html"
    success_url = reverse_lazy("main:index")


class DesignationListView(ListView):
    model = Designation
    template_name = "main/common/object_list.html"

    def get_queryset(self):
        return Designation.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table"] = DesignationTable(self.get_queryset())
        context["form"] = DesignationForm()
        context["create_url"] = reverse_lazy("employees:designation_new")
        context["title"] = "Designation List"
        context["can_add"] = True
        context["is_designation"] = True
        return context


class DesignationDetailView(DetailView):
    model = Designation
    template_name = "main/common/object_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Designation Details"
        return context


class DesignationCreateView(CreateView):
    model = Designation
    form_class = DesignationForm
    template_name = "main/common/object_form.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Designation Create"
        return context

    success_url = reverse_lazy("employees:designation_list")


class DesignationUpdateView(UpdateView):
    model = Designation
    form_class = DesignationForm
    template_name = "main/common/object_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Designation"
        return context

    success_url = reverse_lazy("employees:designation_list")


class DesignationDeleteView(DeleteView):
    model = Designation
    template_name = "main/common/confirm_delete.html"
    success_url = reverse_lazy("employees:designation_list")


class DepartmentListView(ListView):
    model = Department
    template_name = "main/common/object_list.html"

    def get_queryset(self):
        return Department.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table"] = DepartmentTable(self.get_queryset())
        context["form"] = DepartmentForm()
        context["create_url"] = reverse_lazy("employees:department_new")
        context["title"] = "Department List"
        context["can_add"] = True
        context["is_department"] = True
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "main/common/object_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Department Details"
        context["create_url"] = reverse_lazy("employees:department_new")
        context["can_add"] = True
        return context


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "main/common/object_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Department Create"
        return context

    success_url = reverse_lazy("employees:department_list")


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "main/common/object_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Department"
        return context

    success_url = reverse_lazy("employees:department_list")


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "main/common/confirm_delete.html"
    success_url = reverse_lazy("employees:department_list")
