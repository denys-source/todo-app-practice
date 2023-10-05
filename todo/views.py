from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
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
