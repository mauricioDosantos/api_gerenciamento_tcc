from django.db import models


class Usuario(models.Model):
    matricula = models.IntegerField(primary_key=True)
    tipo_usuario = models.ForeignKey("Tipo_usuario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    titulo_graduacao = models.CharField(max_length=70)

    def __str__(self):
        return self.nome


class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField
    descricao = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.descricao


class Usuario_tcc(models.Model):
    matricula_fk = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_tcc_fk = models.ForeignKey('Tcc', on_delete=models.CASCADE)


class Usuario_disciplina(models.Model):
    matricula_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_disciplina_fk = models.ForeignKey('Disciplina', on_delete=models.DO_NOTHING)


class Tcc(models.Model):
    id_tcc = models.AutoField
    titulo = models.TextField()
    resumo = models.TextField()
    introducao = models.TextField()
    referencial_teorico = models.TextField()
    metodologia = models.TextField()
    analise_resultados = models.TextField()
    conclusoes = models.TextField()
    referencia_bibliografica = models.TextField()

    def __str__(self):
        return self.titulo


class Orientacoes(models.Model):
    id_orientacao = models.AutoField
    id_tcc_fk = models.ForeignKey(Tcc, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao


class Disciplina(models.Model):
    id_disciplina = models.AutoField
    nome_disciplina = models.CharField(max_length=70)

    def __str__(self):
        return self.nome_disciplina


class Curso_disciplina(models.Model):
    id_disciplina_fk = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    id_curso_fk = models.ForeignKey('Curso', on_delete=models.CASCADE)


class Curso(models.Model):
    id_curso = models.AutoField
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao