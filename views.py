from django.shortcuts import render
from .forms import DonorForm, PatientForm
from .models import Donor, Patient

# Create your views here.


def main(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        new_donor = DonorForm(request.POST)
        if new_donor.is_valid():
            new_donor.save()
        patients = Patient.objects.all()
        return render(request, "new_donor.html", context={"name": request.POST['name'], "patients": patients})
    form = DonorForm()
    return render(request, "register.html", context={"form": form})


def donate(request):
    return render(request, "donate.html")


def gethelp(request):
    if request.method == "POST":
        new_patient = PatientForm(request.POST)
        if new_patient.is_valid():
            new_patient.save()
        donors = Donor.objects.all()
        return render(request, "new_patient.html", context={"name": request.POST['name'], "donors": donors})
    form = PatientForm()
    return render(request, "gethelp.html", context={"form": form})
