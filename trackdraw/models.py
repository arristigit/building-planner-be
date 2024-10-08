from django.db import models
from django.db.models import JSONField


class Drawing(models.Model):
    title = models.CharField(max_length=255)
    data = JSONField()  # JSONField stores shapes and annotations in JSON format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
