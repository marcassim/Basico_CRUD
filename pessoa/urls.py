from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView
from . import views

urlpatterns = [
    path("", ListaPessoaView.as_view(), name="pessoa.index"),
    path("novo/", PessoaCreateView.as_view(), name="pessoa.novo"),
    path("<int:pk>/editar/", PessoaUpdateView.as_view(), name="pessoa.editar"),
    path("<int:pk>/remover/", PessoaDeleteView.as_view(), name="pessoa.remover"),
    path("<int:pk>/contatos/", views.contatos, name="pessoa.contatos"),
]
