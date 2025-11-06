from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class Home(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "produtos/home.html"
    context_object_name = "produtos"
    ordering = ['nome']

    def get_queryset(self): # método padrão do django para filtragem
        queryset = super().get_queryset()

        pesquisa = self.request.GET.get('pesquisa')

        if pesquisa:
            queryset = queryset.filter(nome__istartswith=pesquisa)

        return queryset

class CriarProduto(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/cadastrar-produto.html"
    success_url = reverse_lazy('home')

class EditarProduto(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/cadastrar-produto.html"
    success_url = reverse_lazy('home')

class CriarCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "produtos/cadastrar-categoria.html"
    success_url = reverse_lazy('home')