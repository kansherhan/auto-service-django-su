from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include

urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include([
                path(
                    "login/",
                    authViews.LoginView.as_view(template_name="registration/login.html"),
                    name="login",
                ),
                path(
                    "logout/",
                    authViews.LogoutView.as_view(template_name="registration/logged_out.html"),
                    name="logout"
                ),
            ]
        ),
    ),
]
