from django.shortcuts import render
from django.http import HttpResponse
from .models import Vaccine, PetVaccination
from rest_framework import viewsets
from .serializers import VaccineSerializer, PetVaccinationSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class PetVaccinationViewSet(viewsets.ModelViewSet):
    queryset = PetVaccination.objects.all()
    serializer_class = PetVaccinationSerializer