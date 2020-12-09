from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=70, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=150, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='foto/%Y/%m')

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
