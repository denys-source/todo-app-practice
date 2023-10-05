from django.urls import path

from todo.views import (
    HomeView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    toggle_completed_status,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle-completed/",
        toggle_completed_status,
        name="toggle-completed",
    ),
]

app_name = "todo"
