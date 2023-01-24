from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fase


class FasesList(ListView):
    model = Fase

    def get_queryset(self):
        return Fase.objects.all()


class FasesUpdate(UpdateView):
    model = Fase
    fields = ['nome', 'jogo']


class FasesCreate(CreateView):
    model = Fase
    fields = ['nome', 'jogo']

    def form_valid(self, form):
        return super(FasesCreate, self).form_valid(form)


class FasesDelete(DeleteView):
    model = Fase
    success_url = reverse_lazy('list_fases')
