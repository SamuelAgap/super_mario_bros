from django.db import models
from django.urls import reverse

from apps.jogos.models import Jogo


class Personagem(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do personagem')
    descricao = models.CharField(max_length=2500, help_text='Descrição do personagem')
    jogos_atrelados = models.ManyToManyField(Jogo)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_personagens')

