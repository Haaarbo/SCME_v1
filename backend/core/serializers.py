from rest_framework import serializers
from .models import Usuario, Material  # Ajuste os nomes conforme seus modelos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Inclui todos os campos. Pode personalizar com uma lista específica.

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
