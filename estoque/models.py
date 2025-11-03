from django.db import models
from usuarios.models import CustomUser
from produtos.models import Produto

# Create your models here.
class MovimentacaoEstoque(models.Model):
    TIPOS = (
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    )

    MOTIVOS = [
        ("COMPRA", "Compra de fornecedor"),
        ("VENDA", "Venda para cliente"),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="movimentacoes")
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.PositiveIntegerField()
    motivo = models.CharField(max_length=255, choices=MOTIVOS)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} ({self.quantidade})"