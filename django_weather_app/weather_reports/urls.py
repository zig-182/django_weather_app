# This imports the path from the in-built django-urls
from django.urls import path

# This imports all the Views from the views.py file
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
