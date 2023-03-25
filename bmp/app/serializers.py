from rest_framework import serializers
from .models import *

class employeserializer(serializers.ModelSerializer):
      class Meta:
            fields="__all__"
            model=employee

class deptserializer(serializers.ModelSerializer):
      class Meta:
            fields="__all__"
            model=department