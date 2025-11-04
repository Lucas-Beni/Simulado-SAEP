from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('cadastrar-produto/', CriarProduto.as_view(), name='criar-produto'),
    path('editar-produto/<int:pk>/', EditarProduto.as_view(), name="editar-produto"),
    path('cadastrar-categoria/', CriarCategoria.as_view(), name='criar-categoria'),
]
