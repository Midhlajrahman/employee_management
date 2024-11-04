from django import forms
from registration.forms import RegistrationForm

from .models import User


class CustomRegistrationForm(RegistrationForm):
    usertype = forms.ChoiceField(
        choices=[
            ("employee", "Employee"),
            ("administrator", "Administrator"),
        ],
        initial="administrator",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    first_name = forms.CharField(
        max_length=128,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=128,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "usertype",
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
