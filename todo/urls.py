from django.urls import path

from todo.views import (
    HomeView,
    TagCreateView,
    TagDeleteView,
    TagListView,
    TagUpdateView,
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
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
