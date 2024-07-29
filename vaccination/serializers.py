from rest_framework import serializers
from .models import Vaccine, PetVaccination

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'

class PetVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetVaccination
        fields = '__all__'

