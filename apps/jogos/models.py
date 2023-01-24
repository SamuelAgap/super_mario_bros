from django.db import models
from django.urls import reverse


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    vendas = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse('list_jogos')

