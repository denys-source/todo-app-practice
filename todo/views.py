from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.forms import TaskForm
from todo.models import Task


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo/home.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")

    def form_valid(self, form: TaskForm) -> HttpResponse:
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "todo/task_delete.html"


@login_required
def toggle_completed_status(request, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        raise PermissionDenied()
    task.completed = not task.completed
    task.save()
    return redirect(request.META.get("HTTP_REFERER", ""))
