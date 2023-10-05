from django.urls import path

from todo.views import HomeView, TaskCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo"
