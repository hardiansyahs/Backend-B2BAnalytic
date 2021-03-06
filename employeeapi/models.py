from django.db import models

# Create your models here.


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE


class Account(models.Model):
    nik = models.IntegerField(max_length=12)
    nama = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
