from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    telefone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.nome
