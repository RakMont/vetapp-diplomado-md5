from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'pet_species', views.PetSpeciesViewSet)
router.register(r'pets', views.PetViewSet)

urlpatterns = [
    path('saludo', views.index),
    path('', include(router.urls)),
    path('owners/pets/<int:owner_id>/', views.owner_pets )
]