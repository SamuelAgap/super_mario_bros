from django.urls import path
from .views import JogosList, JogosUpdate, JogosDelete, JogosCreate


urlpatterns = [
    path('list', JogosList.as_view(), name='list_jogos'),
    path('update/<int:pk>/', JogosUpdate.as_view(), name='update_jogos'),
    path('delete/<int:pk>/', JogosDelete.as_view(), name='delete_jogos'),
    path('create', JogosCreate.as_view(), name='create_jogos'),
]