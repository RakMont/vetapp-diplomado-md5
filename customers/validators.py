from django.core.exceptions import ValidationError
import datetime

def validate_characters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Error, los caracteres especiales en " %(value)s " no estan permitidos', params={'value': value})
        
def validate_phone(value):
    for char in value:
        if not char.isdigit():
            raise ValidationError('Solo se permiten caracteres numéricos')
    if len(value)> 15:
        raise ValidationError('El número de teléfono es demasiado largo')
    
def validate_birth_date(value):
    if value > datetime.date.today():
        raise ValidationError('La fecha de nacimiento no puede ser superior a la fecha actual')
    if (datetime.date.today() - value).days < 30:
        raise ValidationError('La mascota debe tener al menos 30 días de nacida')
               