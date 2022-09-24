import os
from wsgiref import validate
from django.core.exceptions import ValidationError


def allow_images_only_validator(value):
    ext = os.path.splitext(value.name)[1] # índice [1] es la extensión
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensión de archivo no soportada. Extensiones permitidas: ' +str(valid_extensions))