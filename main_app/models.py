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
  birth_date = models.DateField()
  medical_history = models.TextField(max_length=250)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('patient-detail', kwargs={'patient_id': self.id})
  
class Visits(models.Model):
  visit_type = models.CharField(max_length=100)
  date = models.DateField('Visit date')
  height = models.IntegerField()
  weight = models.IntegerField()
  diagnosis = models.CharField(max_length=100)
  treatment = models.TextField(max_length=250)
  again = models.CharField(
    max_length=1,
    choices=OPTIONS,
    default=OPTIONS[1][1]
  )

  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_visit_display()} on {self.date}"