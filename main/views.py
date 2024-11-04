from django.urls import reverse_lazy
from django.views.generic import ListView

from employees.forms import EmployeeCreateForm
from employees.models import Employee
from employees.tables import EmployeeTable


class IndexView(ListView):
    template_name = "main/index.html"

    def get_queryset(self):
        if self.request.user.usertype == "administrator":
            return Employee.objects.all()
        else:
            return Employee.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employees"
        context["can_add"] = True
        context["create_url"] = reverse_lazy("employees:employee_new")
        context["table"] = EmployeeTable(self.get_queryset())
        context["form"] = EmployeeCreateForm()
        context["is_index"] = True

        if self.request.user.usertype != "administrator":
            context["employee"] = Employee.objects.get(user=self.request.user)

        return context
