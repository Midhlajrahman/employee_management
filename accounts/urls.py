from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "user/register/",
        views.CustomRegistrationView.as_view(),
        name="registration_register",
    ),
]
