from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
""""
Web api em cima do protocolo http, para qualquer software que entenda o http
possa se comunicar 
"""


# só com isso ele consegue cadastrar com POST, e consultar com GET
def index(request):
    return render(request, 'api_bd/index.html')


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class TccList(generics.ListCreateAPIView):
    queryset = Tcc.objects.all()
    serializer_class = TccSerializer


class TipoUsuarioList(generics.ListCreateAPIView):
    queryset = Tipo_usuario.objects.all()
    serializer_class = Tipo_usuarioSerializer


class UsuarioTccList(generics.ListCreateAPIView):
    queryset = Usuario_tcc.objects.all()
    serializer_class = Usuario_tccSerializer


class UsuarioDisciplinaList(generics.ListCreateAPIView):
    queryset = Usuario_disciplina.objects.all()
    serializer_class = Usuario_disciplinaSerializer


class OrientacoesList(generics.ListCreateAPIView):
    queryset = Orientacoes.objects.all()
    serializer_class = OrientacoesSerializer


class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class CursoDisciplinaList(generics.ListCreateAPIView):
    queryset = Curso_disciplina.objects.all()
    serializer_class = Curso_disciplinaSerializer


class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer