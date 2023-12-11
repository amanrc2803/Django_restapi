# models.py
from django.db import models

class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    customer_number = models.CharField(max_length=20, unique=True)
    meter_serial_number = models.CharField(max_length=20, unique=True)
