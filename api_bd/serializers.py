from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class TccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tcc
        fields = '__all__'


class Tipo_usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_usuario
        fields = '__all__'


class Usuario_tccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_tcc
        fields = '__all__'


class Usuario_disciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_disciplina
        fields = '__all__'


class OrientacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacoes
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class Curso_disciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso_disciplina
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'