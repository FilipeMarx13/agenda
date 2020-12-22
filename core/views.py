from django.shortcuts import render
from core.models import Evento
# Create your views here.

#Preciso importar redirect from django.shortcuts para usar esse metodo
#def index (request):
 #   return redirect('/agenda/')

def lista_eventos(request):
    #Usuario e evento para este modo seria para filtrar por usuario
    '''
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    # Usuario e evento para este modo seria para filtrar por usuario
    #Este modo evento, busta todos os usuarios'
    '''
    evento = Evento.objects.all()
    dados = {'evento':evento}
    return render(request, 'agenda.html', dados)

