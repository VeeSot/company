
from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    position_title = models.CharField(max_length=100,
                                      verbose_name="Position title")
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"


