from django.urls import path
from .views import FasesList, FasesUpdate, FasesDelete, FasesCreate


urlpatterns = [
    path('list', FasesList.as_view(), name='list_fases'),
    path('update/<int:pk>/', FasesUpdate.as_view(), name='update_fases'),
    path('delete/<int:pk>/', FasesDelete.as_view(), name='delete_fases'),
    path('create', FasesCreate.as_view(), name='create_fases'),
]