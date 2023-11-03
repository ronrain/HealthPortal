from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import VisitForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def patient_index(request):
  patients = Patient.objects.all()
  return render(request, 'patients/index.html', { 'patients': patients })

def patient_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  visit_form = VisitForm()
  return render(request, 'patients/detail.html', {'patient': patient, 'visit_form': visit_form})

class PatientCreate(CreateView):
  model = Patient
  fields = '__all__'
  success_url = '/patients/'

class PatientUpdate(UpdateView):
  model = Patient
  fields = '__all__'

class PatientDelete(DeleteView):
  model = Patient
  success_url = '/patients/'

def add_visit(request, patient_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.patient_id = patient_id
    new_visit.save()
  return redirect('patient-detail', patient_id=patient_id)
