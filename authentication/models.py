from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    handle = models.CharField(blank=False, max_length=24)

    def __str__(self):
        return f'<{self.id}> {self.handle}'