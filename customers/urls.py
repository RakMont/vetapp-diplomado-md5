from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'petspecies', views.PetSpeciesViewSet)
router.register(r'pets', views.PetViewSet)

urlpatterns = [
    path('saludo', views.index),
    path('', include(router.urls))
]