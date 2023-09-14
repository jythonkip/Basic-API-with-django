from rest_framework import serializers
from .models import Persons
from .validators import validate_email_is_unqiue, validate_name_is_unqiue

class PersonsSerializers(serializers.ModelSerializer):
    # detail = serializers.HyperlinkedIdentityField()
    name = serializers.CharField(validators = [validate_name_is_unqiue])
    email = serializers.CharField(validators = [validate_email_is_unqiue])
    
    class Meta:
        model = Persons
        fields = '__all__'

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        return super().create(validated_data)

    