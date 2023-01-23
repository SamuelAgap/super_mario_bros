from django.urls import path
from .views import ola


urlpatterns = [
    path('', ola),
]