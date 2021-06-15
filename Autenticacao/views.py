from rest_framework import viewsets

from Autenticacao.models import Category
from Autenticacao.serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
