from django.db import models

# Create your models here.

# Modelo de um alvo
class Alvo(models.Model):
    nome = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    data_expiracao = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome