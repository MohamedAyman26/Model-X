# custom/views.py
from rest_framework import generics, permissions
from .models import CustomRequest
from .serializers import CustomRequestSerializer, AdminCustomRequestSerializer

class CustomRequestCreateAPIView(generics.CreateAPIView):
    queryset = CustomRequest.objects.all()
    serializer_class = CustomRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyCustomRequestsListAPIView(generics.ListAPIView):
    serializer_class = CustomRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomRequest.objects.filter(user=self.request.user).order_by('-created_at')


class AdminAllCustomRequestsAPIView(generics.ListAPIView):
    serializer_class = AdminCustomRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    queryset = CustomRequest.objects.all().order_by('-created_at')


class AdminCustomRequestUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AdminCustomRequestSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomRequest.objects.all()
