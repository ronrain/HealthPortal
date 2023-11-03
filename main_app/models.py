from django.db import models
from django.urls import reverse

OPTIONS = (
  ('Y', 'Yes'),
  ('N', 'No')
)

class Patient(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  race = models.CharField(max_length=100)
  birth_date = models.DateField('Birth date')
  medical_history = models.TextField(max_length=250)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('patient-detail', kwargs={'patient_id': self.id})
  
class Visits(models.Model):
  date = models.DateField('Visit date')
  visit_type = models.CharField(max_length=100)
  height = models.IntegerField()
  weight = models.IntegerField()
  diagnosis = models.CharField(max_length=100)
  treatment = models.TextField(max_length=250)
  options = models.CharField(
    max_length=1,
    choices=OPTIONS,
    default=OPTIONS[1][1]
  )

  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_option_display()} on {self.visit_type}"
  
  class Meta:
    ordering = ['-date']