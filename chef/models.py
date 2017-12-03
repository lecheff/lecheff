from django.db import models


class Prato(models.Model):
    nome = models.CharField(max_length=50, blank = False)
    descricao_breve = models.CharField(max_length=50, blank = False, default='')

    def __str__(self):
        return self.nome

class Requisitado(models.Model):
    prato = models.ForeignKey(Prato, blank = False)
    imagem = models.CharField(max_length=200, blank = False, default='')
    descricao = models.TextField(default='')

    def __str__(self):
        return str(self.prato)

class Imagem(models.Model):
    titulo = models.CharField(max_length=50, blank = True, null=True)
    url = models.CharField(max_length=200, blank = False, default='')

    def __str__(self):
        return str(self.id)
