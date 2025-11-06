from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "altura", "largura", "peso", "material", "categorias", "is_active"]
        labels = {
            "is_active": "Ativo"
        }

    categorias = forms.ModelMultipleChoiceField(
        queryset=Produto._meta.get_field("categorias").related_model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome",]