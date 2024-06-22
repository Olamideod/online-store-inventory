from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for Django admin interface
    path('api/', include('inventory.urls')),  # Route for API endpoints from 'inventory' app
]

