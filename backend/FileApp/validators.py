from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 104857600:
        raise ValidationError("El maximo a subir es is 100 MB")
    else:
        return value