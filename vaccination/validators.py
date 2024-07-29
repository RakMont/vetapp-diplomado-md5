from django.core.exceptions import ValidationError
import datetime

def validate_characters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Error, los caracteres especiales en " %(value)s " no estan permitidos', params={'value': value})

def validate_dose_quantity(value):
    if value > 10:
        raise ValidationError('La cantidad de veces que la mascota debe recibir la dosis no puede superar 10.') 
    if value <1:
        raise ValidationError('La cantidad de veces que la mascota debe recibir la dosis no puede ser inferior a 1.')
def validate_price(value):
    if value > 200:
        raise ValidationError('El precio no puede ser mayor a 200 $.')
    
def validate_vaccination(value):
    if value > datetime.date.today():
        raise ValidationError('La fecha de vacunación no puede ser posterior a la fecha actual.')
    