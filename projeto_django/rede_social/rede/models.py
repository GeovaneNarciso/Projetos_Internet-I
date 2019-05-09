from django.db import models


class Usuario(models.Model):
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    dt_nasc = models.DateField()

    def __str__(self):
        return self.email


class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contatos = models.ManyToManyField('self')

    class Meta:
        verbose_name_plural = 'Perfil'

    def __str__(self):
        return self.nome


class Postagem(models.Model):
    texto = models.CharField(max_length=255)
    data = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Comentario(models.Model):
    texto = models.CharField(max_length=255)
    data = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Reacao(models.Model):
    tipos = (
        ('C', 'curtir'),
        ('A', 'amar'),
        ('R', 'rir'),
        ('I', 'se impressionar'),
        ('T', 'ficar triste'),
        ('B', 'ficar bravo'))
    data = models.DateField()
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    peso = models.PositiveIntegerField(default=1)
    tipo = models.CharField(default='C', max_length=1, choices=tipos, null=True)

    def __str__(self):
        return self.tipo
