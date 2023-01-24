from django.urls import path
from .views import PersonagemList, PersonagemUpdate, PersonagemDelete, PersonagemCreate


urlpatterns = [
    path('list', PersonagemList.as_view(), name='list_personagens'),
    path('update/<int:pk>/', PersonagemUpdate.as_view(), name='update_personagens'),
    path('delete/<int:pk>/', PersonagemDelete.as_view(), name='delete_personagens'),
    path('create', PersonagemCreate.as_view(), name='create_personagens'),
]