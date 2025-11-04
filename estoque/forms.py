from .models import MovimentacaoEstoque
from django import forms

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ["produto", "quantidade", "motivo"]

    def __init__(self, *args, **kwargs): # método init executado ao criar o formulário
        tipo_movimentacao = kwargs.pop("tipo_movimentacao", None) # tira o campo "tipo_movimentacao" do kwargs caso exista, se não retorna None
        super().__init__(*args, **kwargs)

        if tipo_movimentacao == "entrada": # se o tipo_movimentacao for igual a "entrada"
            self.fields["motivo"].choices = [ # define as opções do campo motivo
                ("COMPRA", "Compra de fornecedor"),
            ]
        elif tipo_movimentacao == "saida": # se o tipo_movimentacao for igual a "saida"
            self.fields["motivo"].choices = [ # define as opções do campo motivo
                ("VENDA", "Venda para cliente"),
            ]