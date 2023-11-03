from django.forms import ModelForm
from .models import Visits

class VisitsForm(ModelForm):
  class Meta:
    model = Visits
    fields = ['visit_type', 'date', 'height', 'weight', 'diagnosis', 'treatment']