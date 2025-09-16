from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import ProdutoFilter
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    # Filtros
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProdutoFilter
    filterset_fields = {
        'estoque': ['exact', 'gte', 'lte']
    }
    search_fields = ['nome', 'categoria__nome']  # Busca textual
    ordering_fields = ['nome', 'preco', 'atualizado_em']  # Ordenação
    ordering = ['-atualizado_em']  # Ordenação padrão
