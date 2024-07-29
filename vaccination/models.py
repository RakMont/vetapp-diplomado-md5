from django.db import models
from customers.models import Pet
from .validators import validate_characters, validate_price, validate_dose_quantity, validate_vaccination

# Create your models here.
class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=100, unique=True, validators=[validate_characters,])
    vaccine_description = models.TextField(null=True, blank=True)
    dose_quantity = models.IntegerField(default=1, validators=[validate_dose_quantity])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    def __str__(self):
        return self.vaccine_name
    
class PetVaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    vaccine_date = models.DateField(validators=[validate_vaccination])
    isPaid = models.BooleanField(default=False)
    description = models.TextField(blank=True,null=True, max_length=200)
