from django.db import models

# Create your models here.


class Perfil:
    def __init__(self, id, nome, email, telefone, nome_empresa):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
