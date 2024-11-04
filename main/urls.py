from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="index"),
]
