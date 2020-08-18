from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    position_title = models.CharField(max_length=100,
                                      verbose_name="Position title")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Branch name")
    facade_image = models.ImageField(null=True,upload_to ='uploads/',
                                     verbose_name="Facade image")
    longitude = models.FloatField(db_index=True,verbose_name="Longitude")
    latitude = models.FloatField(db_index=True,verbose_name="Latitude")
    employees = models.ManyToManyField(Employee, verbose_name='Employees')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
