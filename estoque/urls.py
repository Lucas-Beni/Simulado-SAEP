from django.urls import path
from .views import *

urlpatterns = [
    path('adicionar-entrada/', EntradaCreateView.as_view(), name="adicionar-entrada"),
    path('adicionar-saida/', SaidaCreateView.as_view(), name="adicionar-saida"),
]