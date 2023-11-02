from django.db import models
from django.urls import reverse

class Patient(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  race = models.CharField(max_length=100)
  birth_date = models.DateField()
  medical_history = models.TextField(max_length=250)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('patient-detail', kwargs={'patient_id': self.id})