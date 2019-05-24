from django.db import models
from .models import *


class Registro(models.Model):
    matricula = models.CharField(max_length=255, null=False)
    data_validade = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return self.matricula


class Advogado(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=12, null=False)
    registro = models.OneToOneField(Registro, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nome


class Interessado(models.Model):
    nome = models.CharField(max_length=255, null=False)
    data_nascimento = models.DateField(null=False)
    cpf = models.CharField(max_length=12, null=False)
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    descricao = models.CharField(max_length=255, null=False)
    ativo = models.BooleanField(null=False)

    def __str__(self):
        return self.descricao


class Processo(models.Model):
    numero = models.IntegerField(null=False)
    texto = models.CharField(max_length=255, null=False)
    interessados = models.ManyToManyField(Interessado, null=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.texto


class Apensamento(models.Model):
    processo_apensado = models.ForeignKey(Processo, related_name='processo_apenssado',
                                          on_delete=models.CASCADE, null=False)
    processo_original = models.ForeignKey(Processo, related_name='processo_original',
                                          on_delete=models.CASCADE, null=False)
    data_apensamento = models.DateField(auto_now_add=True, null=False)
