from django.contrib import admin
from django.urls import path, include # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Send all traffic to the 'weather' app's urls.py
    path('', include('weather.urls')), 
]