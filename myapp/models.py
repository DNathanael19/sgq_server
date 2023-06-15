from django.db import models
# Create your models here.
class Aluno(models.Model):
    nome = models.TextField()


    def __str__(self):
        return self.nome


class Experimento_Pratico(models.Model):
    experimento_p = models.IntegerField(primary_key=True)
    temp_ebulicao_p = models.FloatField()
    concentracao_p = models.FloatField(default=None)
    categoria = models.ForeignKey(Aluno, on_delete=models.CASCADE)



