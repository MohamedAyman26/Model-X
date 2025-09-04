# custom/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomRequestCreateAPIView.as_view(), name='custom-request-create'),
    path('my/', views.MyCustomRequestsListAPIView.as_view(), name='custom-request-my-list'),
    path('all/', views.AdminAllCustomRequestsAPIView.as_view(), name='custom-request-admin-list'),
    path('<int:pk>/', views.AdminCustomRequestUpdateAPIView.as_view(), name='custom-request-admin-update'),
]
