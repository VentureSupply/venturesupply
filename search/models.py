from django.db import models

# Create your models here.

class BusinessData(models.Model):
    name = models.CharField(max_length=50)
    certificate = models.CharField(max_length=15)
    file_date = models.DateTimeField('date filed')
    status = models.CharField(max_length=20)
