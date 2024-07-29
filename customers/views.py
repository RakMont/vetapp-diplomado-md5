from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Owner, PetSpecies, Pet
from .serializers import OwnerSerializer, PetSpeciesSerializer, PetSerializer
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
        #print(request)
        #owner_id = request.GET.get("owner_id")
        #owner_id = 1
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

