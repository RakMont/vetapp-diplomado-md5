from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'vaccines', views.VaccineViewSet)
#router.register(r'petvaccination', views.PetVaccinationViewSet)

urlpatterns = [
    path('', include(router.urls))
]