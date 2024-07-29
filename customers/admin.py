from django.contrib import admin
from .models import Owner, PetSpecies, Pet


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name','last_name', 'email',
                     'phone_number')
    search_fields = ('name', 'last_name')
    ordering = ('name',)

class PetSpeciesAdmin(admin.ModelAdmin):
    ordering = ('name',)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',
                     'species','breed',
                      'weight','sex', 'birth_date')
    list_filter = ('species','sex')
    search_fields = ('name', 'owner')
    ordering = ('name',)
# Register your models here.
admin.site.register(Owner, OwnerAdmin)
admin.site.register(PetSpecies, PetSpeciesAdmin)
admin.site.register(Pet, PetAdmin)