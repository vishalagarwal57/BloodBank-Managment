from django.forms import ModelForm
from .models import Donor, Patient

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
