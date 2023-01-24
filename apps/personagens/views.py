from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Personagem


class PersonagemList(ListView):
    model = Personagem

    def get_queryset(self):
        return Personagem.objects.all()


class PersonagemUpdate(UpdateView):
    model = Personagem
    fields = ['nome', 'descricao', 'jogos_atrelados']


class PersonagemCreate(CreateView):
    model = Personagem
    fields = ['nome', 'descricao', 'jogos_atrelados']

    def form_valid(self, form):
        return super(PersonagemCreate, self).form_valid(form)


class PersonagemDelete(DeleteView):
    model = Personagem
    success_url = reverse_lazy('list_personagens')
