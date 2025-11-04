from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Produto, Categoria

class CustomClearableFileInput(ClearableFileInput):
    initial_text = "Imagem atual"
    input_text = "Alterar"
    clear_checkbox_label = "Remover"

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "altura", "largura", "peso", "material", "categorias", "imagem_principal", "is_active"]
        widgets = {
            "imagem_principal": CustomClearableFileInput
        }
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