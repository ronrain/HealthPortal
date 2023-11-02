from django.db import models

class Patient(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  race = models.CharField(max_length=100)
  birth_date = models.DateField()
  medical_history = models.TextField(max_length=250)
  description = models.TextField(max_length=250)
