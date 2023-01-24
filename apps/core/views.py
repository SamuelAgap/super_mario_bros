from django.shortcuts import render
from apps.jogos.models import Jogo

def home(request):
    data = {}
    data['jogo', 'request'] = Jogo.objects.last()

    return render(request, 'core/index.html', data)
