from django.db import models

class TypeProveedor(models.TextChoices):
    Hotel       = "Hotel"
    Pista       = "Pista"
    Complemento = "Complemento"


class Proveedor(models.Model):
    name           = models.CharField(max_length = 128)
    email          = models.EmailField()
    phone          = models.CharField(max_length = 128)
    type_proveedor = models.TextField(choices=TypeProveedor.choices)
    active         = models.BooleanField()
    created_at     = models.DateTimeField(auto_now = True)
    update_at      = models.DateTimeField(auto_now_add = True)

    
