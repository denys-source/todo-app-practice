from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import QuerySet
from django.http import HttpRequest
from todo.middleware import get_current_user

from todo.models import Tag, Task


class LoginForm(AuthenticationForm):
    def __init__(
        self, request: HttpRequest | None = ..., *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(request, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-input"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=QuerySet(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["tags"].queryset = Tag.objects.filter(
            created_by=get_current_user()
        )

        for visible in self.visible_fields():
            if not isinstance(visible.field, forms.ModelMultipleChoiceField):
                visible.field.widget.attrs["class"] = "form-input"

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {"deadline": forms.widgets.DateInput(attrs={"type": "date"})}
