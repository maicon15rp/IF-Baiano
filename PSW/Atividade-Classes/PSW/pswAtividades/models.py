from django.db import models

# Usei os tipos de dados do diagrama: float, int e string
class Pessoa(models.Model):
    nome = models.CharField(
        max_length=100
    )
    endereco = models.CharField(
        max_length=100
    )
    telefone = models.CharField(
        max_length=9
    )

    def cadastrar():
        return True

class Curso(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(
        max_length=100
    )
    def cadastrar():
        return True

class Disciplina(models.Model):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE
    )
    codigo = models.IntegerField()
    descricao = models.CharField(
        max_length=100
    )
    carga_horaria = models.IntegerField()
    ementa = models.CharField(
        max_length=100
    )
    bibliografia = models.CharField(
        max_length=100
    )

    def cadastrar():
        return True


class PreRequisito(models.Model):
    disciplina = models.ForeignKey(
        Disciplina, 
        on_delete=models.CASCADE, 
        related_name='disciplina'
    )
    disciplina_pre_requisito = models.ForeignKey(
        Disciplina, 
        on_delete=models.CASCADE, 
        related_name='disciplina_pre_requisito'
    ) 

class Turma(models.Model):
    disciplina = models.OneToOneField(
        Disciplina, 
        on_delete=models.CASCADE
    )
    ano = models.IntegerField()
    semestre = models.IntegerField()
    dia_semana = models.IntegerField()
    horarios = models.CharField(
        max_length=100
    )
    def abrirTurma():
        return True

    def alocarProfessor():
        return True

    def matricularAluno():
        return True

    def emitirDiario():
        return True

class Aluno(Pessoa):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE
    )
    matricula = models.CharField(
        max_length=30
    )
    situacao = models.CharField(
        max_length=30
    )
    avaliacoes = models.ManyToManyField(
        Turma,
        related_name="alunoAvaliacoes",
        through="Avaliacao"
    )

    def matricularCurso():
        return True
        
    def trancar():
        return True
        
    def formar():
        return True
        
    def evadir():
        return True
        
    def formar():
        return True

    def obterAvaliacoes():
        return True
        
    def emitirHistorico():
        return True

class Professor(Pessoa):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE
    )
    titulacao_maxima = models.CharField(
        max_length=100
    )

class Avaliacao(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='Aluno_avaliacao'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='Aluno_avaliacao'
    )
    nota_1 = models.FloatField(
        max_length=10,
        blank=False,
        null=False,
    )
    nota_2 = models.FloatField(
        max_length=10,
        blank=False,
        null=False,
    )
    nota_prova_final = models.FloatField(
        max_length=10,
        blank=False,
        null=False,
    )
    frequencia = models.IntegerField()
        
    def lancarAvaliacao():
        return True
        
    def calcularAprovacao():
        return True

# Create your models here.
