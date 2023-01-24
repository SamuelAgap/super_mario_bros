from django.views.generic import ListView
from apps.jogos.models import Jogo


class Home(ListView):
    model = Jogo
    template_name = 'home.html'

    def get_queryset(self):
        return Jogo.objects.all().order_by('-pk')


class SaibaMais(ListView):
    model = Jogo
    template_name = 'saiba_mais.html'

    def get_queryset(self):
        return Jogo.objects.all()
