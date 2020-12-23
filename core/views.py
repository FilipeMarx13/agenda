from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

#Preciso importar redirect from django.shortcuts para usar esse metodo
#def index (request):
 #   return redirect('/agenda/')


def login_user(request):
    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "User or Password incorret")
    return redirect('/')


@login_required(login_url='/login/')

def lista_eventos(request):
    #Usuario e evento para este modo seria para filtrar por usuario

    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    # Usuario e evento para este modo seria para filtrar por usuario
    #Este modo evento, busta todos os usuarios'

    #evento = Evento.objects.all()
    dados = {'evento':evento}
    return render(request, 'agenda.html', dados)

