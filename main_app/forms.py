from django.forms import ModelForm
from .models import Visits

class VisitForm(ModelForm):
  class Meta:
    model = Visits
    fields = ['visit_type', 'date', 'height', 'weight', 'diagnosis', 'treatment']