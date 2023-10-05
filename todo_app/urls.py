from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.conf import settings

from todo.forms import LoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls", namespace="todo")),
    path(
        "accounts/login/",
        LoginView.as_view(
            redirect_authenticated_user=True, authentication_form=LoginForm
        ),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
] + (
    [path("__debug__/", include("debug_toolbar.urls"))]
    if settings.DEBUG
    else []
)
