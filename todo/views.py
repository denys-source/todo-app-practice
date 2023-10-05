from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.models import Task


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo/home.html"
