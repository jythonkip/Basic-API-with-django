from .models import Persons
from rest_framework import serializers



def validate_name_is_unqiue(value):
    name = Persons.objects.filter(name__iexact = value)
    if name.exists():
        raise serializers.ValidationError('Ooops, this name already exists!!')
    return value

def validate_email_is_unqiue(value):
    email = Persons.objects.filter(email__iexact = value)
    if email.exists():
        raise serializers.ValidationError("An account has already been created with this email")
    return value 