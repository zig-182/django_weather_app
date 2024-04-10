from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # the default path for the admin site
    path('admin/', admin.site.urls),
    
    # this points django to the weather_reports app urls
    path('', include('weather_reports.urls')),
]
