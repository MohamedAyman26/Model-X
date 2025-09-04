from rest_framework import serializers
from .models import UserMeasurement

class UserMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMeasurement
        fields = ['height', 'weight', 'size']