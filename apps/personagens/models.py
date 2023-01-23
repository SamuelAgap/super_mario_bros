from django.db import models


class Personagem(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do personagem')

    def __str__(self):
        return self.nome
