from django.db import models
from django.utils import timezone

import datetime

class Pet(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)
    breed = models.CharField(max_length=50)
    weight_in_pounds = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    # Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date_of_appointment = models.DateField(null=True, blank=True)
    duration_minutes = models.IntegerField(default=0)
    special_instructions = models.CharField(max_length=2000)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
    appointment_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.appointment_name
