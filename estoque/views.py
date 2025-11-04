from django.shortcuts import render
from django.views.generic import CreateView
from .models import MovimentacaoEstoque
from .forms import MovimentacaoEstoqueForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = MovimentacaoEstoque
    form_class = MovimentacaoEstoqueForm
    template_name = "estoque/movimentacao_estoque.html"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["tipo_movimentacao"] = "entrada"
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_movimentacao"] = "entrada"
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.tipo = "ENTRADA"
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser


class SaidaCreateView(LoginRequiredMixin, CreateView):
    model = MovimentacaoEstoque
    form_class = MovimentacaoEstoqueForm
    template_name = "estoque/movimentacao_estoque.html"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["tipo_movimentacao"] = "saida"
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo_movimentacao"] = "saida"
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.tipo = "SAIDA"
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser