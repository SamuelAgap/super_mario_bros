from django.db import models
from apps.jogos.models import Jogo


class Fase(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da fase')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
