from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/order/', include('order.urls')),
    path('api/measurements/', include('measurements.urls')),
    path('api/custom-request/', include('custom.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
