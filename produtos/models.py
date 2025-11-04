from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(null=True, blank=True)
    altura = models.DecimalField(decimal_places=1, max_digits=5)
    largura = models.DecimalField(decimal_places=1, max_digits=5)
    peso = models.DecimalField(decimal_places=1, max_digits=5)
    material = models.CharField(max_length=20)
    categorias = models.ManyToManyField(Categoria, related_name="produtos")
    imagem_principal = models.ImageField(upload_to="produtos/principal/", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def estoque_atual(self):
        entradas = self.movimentacoes.filter(tipo="ENTRADA").aggregate(total=models.Sum("quantidade"))["total"] or 0
        saidas = self.movimentacoes.filter(tipo="SAIDA").aggregate(total=models.Sum("quantidade"))["total"] or 0
        return entradas - saidas
    
    @property
    def estoque_seguranca(self):
        saidas = self.movimentacoes.filter(tipo="SAIDA")
        total_saidas = saidas.aggregate(total=models.Sum("quantidade"))["total"] or 0
        qtd_saidas = saidas.count() or 1

        media_saidas = total_saidas / qtd_saidas
        return int(media_saidas)


    def __str__(self):
        return f'{self.nome}: {self.descricao}'