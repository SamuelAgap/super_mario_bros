from django.db import models


class Jogo(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do jogo')

    def __str__(self):
        return self.nome

