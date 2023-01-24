from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Jogo


class JogosList(ListView):
    model = Jogo

    def get_queryset(self):
        return Jogo.objects.all()


class JogosUpdate(UpdateView):
    model = Jogo
    fields = ['nome', 'ano', 'vendas', 'estilo', 'descricao', 'imagem']


class JogosCreate(CreateView):
    model = Jogo
    fields = ['nome', 'ano', 'vendas', 'estilo', 'descricao', 'imagem']

    def form_valid(self, form):
        return super(JogosCreate, self).form_valid(form)


class JogosDelete(DeleteView):
    model = Jogo
    success_url = reverse_lazy('list_jogos')
