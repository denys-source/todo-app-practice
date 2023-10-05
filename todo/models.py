from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

from todo.middleware import get_current_user


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="tags", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs) -> None:
        self.user = get_current_user()
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("-created_at", "completed")

    def __str__(self) -> str:
        return self.content
