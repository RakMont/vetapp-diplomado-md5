from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Owner, PetSpecies, Pet
from .serializers import OwnerSerializer, PetSpeciesSerializer, PetSerializer
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