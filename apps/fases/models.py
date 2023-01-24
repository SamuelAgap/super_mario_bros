from django.db import models
from django.urls import reverse
from apps.jogos.models import Jogo


class Fase(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da fase')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_fases')
