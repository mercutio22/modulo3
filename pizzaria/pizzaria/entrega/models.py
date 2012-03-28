#coding=utf-8
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    fone = models.CharField(max_length=16, db_index=True)
    ramal = models.CharField(max_length=4, blank=True)
    email = models.EmailField(blank=True)
    logradouro = models.CharField(max_length=32, db_index=True)
    numero = models.PositiveIntegerField(u'número', db_index=True)
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(verbose_name=u'Observação')
    
    class Meta:
        #Os campos a seguir devem ser únicos concatenados!
        unique_together = ('fone', 'ramal') 

    def __unicode__(self):
        return self.nome

    def endereco(self):
        return '%s, %s' % (self.logradouro, self.numero)
    endereco.short_description = u'Endereço' #TRUQUE!!!!

class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add=True) 
    # a opcao auto_now funcionaria sempre que o pedido fosse modificado
    cliente = models.ForeignKey(Cliente)
    pronto = models.BooleanField(default=False)
    entregador = models.ForeignKey('Entregador', null=True, blank=True)
    partida = models.TimeField(null=True, blank=True)

class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'entregadores'
