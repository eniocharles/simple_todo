from django.db import models
from django.core.exceptions import ValidationError

def validate_mesa(value):
    if value < 1 or value > 10: 
        raise ValidationError("Número da mesa deve estar entre 1 e 10.")

class Pedidos(models.Model):
    mesa = models.IntegerField(validators=[validate_mesa])
    pedido = models.TextField()
    horario = models.TimeField()    