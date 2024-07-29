from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Owner, PetSpecies, Pet
from vaccination.models import PetVaccination
from .serializers import OwnerSerializer, ReportPetVaccinationsSerializer, PetSpeciesSerializer, PetSerializer
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PetSpeciesViewSet(viewsets.ModelViewSet):
    queryset = PetSpecies.objects.all()
    serializer_class = PetSpeciesSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

@api_view(['GET'])
def owner_pets(request, owner_id):
    """
    Mascotas de un Propietario
    """
    try:
        pets = Pet.objects.filter(owner_id=owner_id)
        return JsonResponse(
            PetSerializer(pets, many=True).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def pets_vaccinations(request, pet_id):
    """
    Vacunas de las mascotas de un propietario
    """
    try:
        pet = Pet.objects.get(id=pet_id)
        vaccinations = PetVaccination.objects.filter(pet_id = pet_id)
        return JsonResponse(
            ReportPetVaccinationsSerializer({
                "pet": pet,
                "total_vaccinations": vaccinations.count(),
                "vaccinations": vaccinations
            }).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )