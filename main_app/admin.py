from django.contrib import admin
# import your models here
from .models import Patient

# Register your models here
admin.site.register(Patient)