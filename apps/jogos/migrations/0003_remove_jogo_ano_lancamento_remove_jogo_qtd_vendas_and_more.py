# Generated by Django 4.1.5 on 2023-01-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0002_jogo_ano_lancamento_jogo_estilo_jogo_qtd_vendas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='ano_lancamento',
        ),
        migrations.RemoveField(
            model_name='jogo',
            name='qtd_vendas',
        ),
        migrations.AddField(
            model_name='jogo',
            name='ano',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogo',
            name='vendas',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jogo',
            name='estilo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]