from django.contrib import admin

from .models import Department, Designation, Employee


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    search_fields = ["name"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "department_lead", "is_active"]
    search_fields = ["name"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "personal_email",
        "department",
        "designation",
        "is_active",
    ]
    search_fields = ["department__name", "designation__name"]
