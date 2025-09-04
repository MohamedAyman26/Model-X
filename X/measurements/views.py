from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import UserMeasurement
from .serializers import UserMeasurementSerializer
from rest_framework.response import Response
from rest_framework import status

class MeasurementCreateAPIView(generics.CreateAPIView):
    serializer_class = UserMeasurementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            height = serializer.validated_data['height']
            weight = serializer.validated_data['weight']
            # Determine size based on height and weight
            if height < 160:
                size = 'S'
            elif height < 180:
                size = 'M'
            else:
                size = 'L'
            serializer.save(size=size)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)