from django.db import models

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField()
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    CPF = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.usuario}'
    def clean(self):
        ...

