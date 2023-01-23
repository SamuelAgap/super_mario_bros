from django.db import models


class Jogo(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do jogo')
    ano_lancamento = models.CharField(max_length=100, help_text='Ano de lançamento')
    qtd_vendas = models.CharField(max_length=100, help_text='Quantidade de vendas')
    estilo = models.CharField(max_length=100, help_text='Estilo de jogo')

    def __str__(self):
        return self.nome

