from django.contrib import admin
from .models import Donor, Blood, Patient

# Register your models here.

admin.site.register(Donor)
admin.site.register(Blood)
admin.site.register(Patient)