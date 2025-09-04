# custom/serializers.py
from rest_framework import serializers
from .models import CustomRequest

class CustomRequestSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = CustomRequest
        fields = ['id', 'user', 'image', 'description2', 'status', 'status_display', 'created_at']
        read_only_fields = ['id', 'user', 'created_at', 'status']
    
    def create(self, validated_data):
        user = self.context['request'].user
        return CustomRequest.objects.create(user=user, **validated_data)


class AdminCustomRequestSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = CustomRequest
        fields = ['id', 'user', 'user_username', 'image', 'description2', 'status', 'status_display', 'created_at']
