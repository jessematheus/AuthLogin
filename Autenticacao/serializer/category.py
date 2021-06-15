from rest_framework import serializers

from Autenticacao.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "description"]
