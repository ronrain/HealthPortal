from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Patient


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def patient_index(request):
  patients = Patient.objects.all()
  return render(request, 'patients/index.html', { 'patients': patients })

def patient_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  return render(request, 'patients/detail.html', {'patient': patient})

class PatientCreate(CreateView):
  model = Patient
  fields = '__all__'
  success_url = '/patients/'

class PatientUpdate(UpdateView):
  model = Patient
  fields = '__all__'