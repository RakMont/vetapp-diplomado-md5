from django.contrib import admin
from .models import Vaccine, PetVaccination
# Register your models here.

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_name', 'vaccine_description',
                     'dose_quantity', 'price')
    search_fields = ('vaccine_name',)
    ordering = ('vaccine_name', 'price',)
class PetVaccinationAdmin(admin.ModelAdmin):
    list_display = ('pet', 'vaccine', 'vaccine_date',
                     'isPaid', 'description')
    list_filter = ('isPaid',)
    search_fields = ('pet', 'vaccine')
    ordering = ('vaccine_date',)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(PetVaccination, PetVaccinationAdmin)