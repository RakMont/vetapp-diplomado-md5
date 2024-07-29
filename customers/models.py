from django.db import models
from .validators import validate_characters, validate_phone, validate_birth_date
# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100, validators=[validate_characters,])
    last_name = models.CharField(max_length=100,validators=[validate_characters,])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True,validators=[validate_phone,])
    address = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class PetSex(models.TextChoices):
    FEMALE = 'f', 'Female'
    MALE ='m', 'Male' 

class PetSpecies(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
class Pet(models.Model):
    name = models.CharField(max_length=100, validators=[validate_characters,])
    species = models.ForeignKey(PetSpecies, on_delete=models.SET_NULL, null=True)
    breed = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=10)
    birth_date = models.DateField(validators=[validate_birth_date,])
    sex = models.CharField(
        max_length=5,
        choices=PetSex.choices,
        default=PetSex.MALE)
    description = models.TextField( null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name