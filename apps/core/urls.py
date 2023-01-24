from django.urls import path
from .views import Home, SaibaMais

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('saiba_mais/<int:pk>/', SaibaMais.as_view(), name='saiba_mais'),
]