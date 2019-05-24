"""
from processo.models import *

r1 = Registro.objects.create(matricula='100')

a1 = Advogado.objects.create(nome='Joao Carlos', cpf='11122233344', registro=r1)

interessado = Interessado.objects.create(nome='Maria Nunes', data_nascimento='1985-01-01', cpf='22233344455', advo
gado=a1)

tipo = Tipo.objects.create(descricao='administrativo', ativo=True)

processo_1 = Processo.objects.create(numero=123, texto='Processo de tal pessoa...', tipo=tipo)
processo_1.interessados.set([interessado])


inter_2 = Interessado.objects.create(nome='Paulo Clara', data_nascimento='1990-01-01', cpf='22233344488', advogado=a1)

processo_2 = Processo.objects.create(numero=345, texto='Processo de fulano...', tipo=tipo)
processo_2.interessados.set([inter_2])

apensamento_1 = Apensamento.objects.create(processo_apensado=processo_2, processo_original=processo_1)
"""
