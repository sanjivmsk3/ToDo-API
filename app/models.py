from django.db import models
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    des = models.TextField(null=True, blank=True, verbose_name="Descriptions")
    author = models.CharField(max_length=100, null=True, blank=True, verbose_name="Created By")
    created = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    updated = models.DateTimeField(default=timezone.now, verbose_name="Updated Date")

    def __str__(self) -> str:
        return self.title
        