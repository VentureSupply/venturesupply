from django.db import models

# Create your models here.

class CorporationNameSearch(models.Model):
    entity_number = models.CharField(max_length=50)
    date_filed = models.DateTimeField('date filed')
    status = models.CharField(max_length=20)
    entity_name = models.CharField(max_length=20)
    agent_for_service = models.CharField(max_length=20)
