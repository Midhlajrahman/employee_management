from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    ordering = ("username",)
    list_display = (
        "username",
        "first_name",
        "usertype",
        "is_active",
        "date_joined",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("username",)
    readonly_fields = ("last_login", "date_joined", "pk")
    search_fields = ["username"]
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
        "usertype",
    )
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "usertype",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Groups", {"fields": ("groups",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, MyUserAdmin)
