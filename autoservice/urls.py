from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("spare_parts/", include("spare_parts.urls")),
    path("auth/", include([
                path(
                    "login/",
                    authViews.LoginView.as_view(template_name="pages/auth/login.html"),
                    name="login",
                ),
                path(
                    "logout/",
                    authViews.LogoutView.as_view(),
                    name="logout"
                ),
            ]
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
