from django.contrib import admin
# import your models here
from .models import Patient, Visits

# Register your models here
admin.site.register(Patient)
admin.site.register(Visits)
