import django_tables2 as tables
from django_tables2 import columns

from .models import Department, Designation, Employee


class HybridTable(tables.Table):
    action = columns.TemplateColumn(
        """
        <div class="btn-group">
            <a class="btn btn-default mx-1 btn-sm" title='View' href="{{record.get_absolute_url}}"><i class="fa fa-eye"></i></a>
            <a class="btn btn-default mx-1 btn-sm" title='Edit' href="{{record.get_update_url}}"><i class="fa fa-edit"></i></a>
            <a class="btn btn-default mx-1 btn-sm" title='Delete' href="{{record.get_delete_url}}"><i class="fa fa-trash"></i></a>
        </div>
        """,
        orderable=False,
    )


class EmployeeTable(HybridTable):
    class Meta:
        model = Employee
        fields = (
            "employee_id",
            "fullname",
            "gender",
            "department",
            "designation",
            "marital_status",
            "mobile",
            "date_of_birth",
            "religion",
        )
        attrs = {
            "class": "table key-buttons border-bottom table-hover table-striped table-bordered"
        }


class DesignationTable(HybridTable):

    action = columns.TemplateColumn(
        """
        <div class="btn-group">
            <a class="btn btn-default mx-1 btn-sm" title='Edit' href="{{record.get_update_url}}"><i class="fa fa-edit"></i></a>
            <a class="btn btn-default mx-1 btn-sm" title='Delete' href="{{record.get_delete_url}}"><i class="fa fa-trash"></i></a>
        </div>
        """,
        orderable=False,
    )

    class Meta:
        model = Designation
        fields = (
            "name",
            "description",
        )
        attrs = {
            "class": "table key-buttons border-bottom table-hover table-striped table-bordered"
        }


class DepartmentTable(HybridTable):

    action = columns.TemplateColumn(
        """
        <div class="btn-group">
            <a class="btn btn-default mx-1 btn-sm" title='Edit' href="{{record.get_update_url}}"><i class="fa fa-edit"></i></a>
            <a class="btn btn-default mx-1 btn-sm" title='Delete' href="{{record.get_delete_url}}"><i class="fa fa-trash"></i></a>
        </div>
        """,
        orderable=False,
    )

    class Meta:
        model = Department
        fields = (
            "name",
            "department_lead",
            "description",
        )
        attrs = {
            "class": "table key-buttons border-bottom table-hover table-striped table-bordered"
        }
