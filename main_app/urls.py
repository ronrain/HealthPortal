from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('patients/', views.patient_index, name='patient-index'),
  path('patients/<int:patient_id>/', views.patient_detail, name='patient-detail'),
  path('patients/create/', views.PatientCreate.as_view(), name='patient-create'),
  path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient-update'),
  path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient-delete'),
]