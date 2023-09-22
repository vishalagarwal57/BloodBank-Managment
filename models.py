from django.db import models

# Create your models here.

class Blood(models.Model):
    blood_group = models.CharField(max_length=5)
    
    def __str__(self):
        return self.blood_group

class Donor(models.Model):
    name = models.CharField(max_length=50, null=False)
    blood_group = models.ForeignKey(Blood, on_delete=models.PROTECT, default=None)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=50, null=False)
    blood_group = models.ForeignKey(Blood, on_delete=models.PROTECT, default=None)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
