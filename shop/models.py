from django.db import models
import uuid

from django.urls import reverse

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageFIeld(upload_to = 'category', blank=True)
