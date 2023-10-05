from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest


class LoginForm(AuthenticationForm):
    def __init__(
        self, request: HttpRequest | None = ..., *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(request, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-input"
