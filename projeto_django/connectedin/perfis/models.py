from django.db import models


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome

    def convidar(self, perfil_convidado):
        convite = Convite(convidador=self, convidado=perfil_convidado)
        convite.save()


class Convite(models.Model):
    convidador = models.ForeignKey(Perfil, related_name='convites_feitos', on_delete=models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos', on_delete=models.CASCADE)
