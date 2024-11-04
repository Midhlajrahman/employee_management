from django import forms

from accounts.models import User

from .models import Department, Designation, Employee


class EmployeeCreateForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=128, required=False)
    last_name = forms.CharField(max_length=128, required=False)
    personal_email = forms.EmailField(max_length=128, required=False)

    class Meta:
        model = Employee
        fields = [
            "username",
            "password",
            "employee_id",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "marital_status",
            "personal_email",
            "mobile",
            "whatsapp",
            "date_of_birth",
            "religion",
            "photo",
            "official_email",
            "department",
            "designation",
            "father_name",
            "father_mobile",
            "mother_name",
            "guardian_name",
            "guardian_mobile",
            "relationship_with_employee",
            "date_of_joining",
            "date_of_confirmation",
            "type_of_residence",
            "residence_name",
            "residential_address",
            "residence_contact",
            "residential_postal_code",
            "permanent_address",
            "permanent_postal_code",
            "bank_name",
            "account_name",
            "account_number",
            "ifsc_code",
            "bank_branch",
            "pan_number",
            "employment_type",
            "blood_group",
            "basic_salary",
            "hra",
            "other_allowance",
            "transportation_allowance",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "date_of_joining": forms.DateInput(attrs={"type": "date"}),
            "date_of_confirmation": forms.DateInput(attrs={"type": "date"}),
            "photo": forms.FileInput(),
        }

    def save(self, commit=True):
        username = self.cleaned_data.pop("username")
        password = self.cleaned_data.pop("password")

        user = User(username=username)
        user.set_password(password)

        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        user.email = self.cleaned_data.get("personal_email", "")
        user.usertype = "employee"

        if commit:
            user.save()

        employee = super().save(commit=False)
        employee.user = user

        if commit:
            employee.save()

        return employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "marital_status",
            "personal_email",
            "mobile",
            "whatsapp",
            "date_of_birth",
            "religion",
            "photo",
            "official_email",
            "department",
            "designation",
            "father_name",
            "father_mobile",
            "mother_name",
            "guardian_name",
            "guardian_mobile",
            "relationship_with_employee",
            "date_of_joining",
            "date_of_confirmation",
            "type_of_residence",
            "residence_name",
            "residential_address",
            "residence_contact",
            "residential_postal_code",
            "permanent_address",
            "permanent_postal_code",
            "bank_name",
            "account_name",
            "account_number",
            "ifsc_code",
            "bank_branch",
            "pan_number",
            "employment_type",
            "blood_group",
            "basic_salary",
            "hra",
            "other_allowance",
            "transportation_allowance",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "date_of_joining": forms.DateInput(attrs={"type": "date"}),
            "date_of_confirmation": forms.DateInput(attrs={"type": "date"}),
            "photo": forms.FileInput(),
        }


class DesignationForm(forms.ModelForm):

    class Meta:
        model = Designation
        fields = [
            "name",
            "description",
        ]


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            "name",
            "department_lead",
            "description",
        ]
