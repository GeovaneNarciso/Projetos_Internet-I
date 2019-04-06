from django.shortcuts import render
from .models import Perfil
# Create your views here.


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
    perfil = get_perfil(perfil_id)
    return render(request, 'perfil.html', {'perfil': perfil})


def get_perfil(perfil_id):
    if perfil_id == 1:
        return Perfil(id=1, nome='Geovane', email='g@gmail.com', telefone='98765432', nome_empresa='G Enterprise')
    elif perfil_id == 2:
        return Perfil(id=2, nome='Pazuzu', email='666@gmail.com', telefone='999', nome_empresa='Mr.Satan')
