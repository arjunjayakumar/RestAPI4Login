from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import test

class testserializer(ModelSerializer):
    class Meta:
        model=test
        fields="__all__"