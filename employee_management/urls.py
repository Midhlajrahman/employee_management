# Define urlpatterns in project/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("main.urls", namespace="main")),
        path("accounts/", include("registration.backends.simple.urls")),
        path("accounts/", include("accounts.urls", namespace="accounts")),
        path("employees/", include("employees.urls", namespace="employees")),
        path(
            "sitemap.xml",
            TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),
        ),
        path(
            "robots.txt",
            TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Employee Management Administration"
admin.site.site_title = "Employee Management Admin Portal"
admin.site.index_title = "Welcome to Employee Management Admin Portal"
