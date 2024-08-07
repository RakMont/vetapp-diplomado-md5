from rest_framework import serializers
from .models import Owner, PetSpecies, Pet
from vaccination.serializers import PetVaccinationSerializer
#from .validators import validate_characters, validate_phone, validate_birth_date

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class PetSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSpecies
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
class ReportPetVaccinationsSerializer(serializers.Serializer):
    pet = PetSerializer()
    total_vaccinations = serializers.IntegerField()
    vaccinations = PetVaccinationSerializer(many=True)
