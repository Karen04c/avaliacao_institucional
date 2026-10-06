from django.db import models


class Avaliacao(models.Model):
    nota = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ("PENDENTE", "Pendente"),
            ("RESPONDIDA", "Respondida"),
        ],
        default="PENDENTE",
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    aluno = models.ForeignKey(
        "aluno.Aluno",
        on_delete=models.CASCADE,
    )  

    disciplina = models.ForeignKey(
        "disciplina.Disciplina",
        on_delete=models.CASCADE,
    )  