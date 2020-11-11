from django.urls import path
from . import views


urlpatterns = [
    # as_view() executa isso como uma função, entendi isso com uma função
    #nome urls sempre no plural
    path('', views.index, name='index'),
    path('usuarios/', views.UsuarioList.as_view(), name='usuarios'),
    path('tccs/', views.TccList.as_view(), name='tccs'),
    path('usuarios_tcc/', views.UsuarioTccList.as_view(), name='usuarios_tcc'),
    path('usuarios_disciplina/', views.UsuarioDisciplinaList.as_view(), name='usuarios_disciplina'),
    path('disciplinas_curso/', views.CursoDisciplinaList.as_view(), name='disciplinas_curso'),
    path('cursos/', views.CursoList.as_view(), name='cursos'),
    path('disciplinas/', views.DisciplinaList.as_view(), name='disciplinas'),
    path('orientacoes/', views.OrientacoesList.as_view(), name='orientacoes'),
]