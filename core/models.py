from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField(blank=True, null=True ) #campo pode ficar em branco
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_craiacao = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criacao') #Insere a data e hora automaticamente
  #VERBOSE_NAME SERVE PARA PERSONALIZAR O TITULO QUE VOCE DESEJA NO PAINEL
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Evento'
    def __str__(self):
        return self.titulo #Serve para eu usar o titulo na parte principal pois antes fica como objeto1 nome por default
