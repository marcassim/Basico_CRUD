from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import PessoaForm
from .models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by("nome_completo")


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = "/pessoas/"


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = "/pessoas/"


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = "/pessoas/"
