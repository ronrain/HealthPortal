from django.shortcuts import render

from django.http import HttpResponse


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def patient_index(request):
  return render(request, 'patients/index.html', { 'patients': patients })

# Add the Cat class & list and view function below the imports
class Patient:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, race, description, age, birth_date, gender, medical_history):
    self.name = name
    self.race = race
    self.description = description
    self.age = age
    self.birth_date=birth_date
    self.gender=gender
    self.medical_history=medical_history

patients = [
  Patient('Lolo', 'white', 'moderate bipolar', 3, '3/31/1998', 'male', 'none'),
]