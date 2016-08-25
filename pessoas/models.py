from django.db import models
from default.models import Pessoa


class Cliente(Pessoa):
    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'


class Fornecedor(Pessoa):
    class Meta:
        verbose_name = u'Fornecedor'
        verbose_name_plural = u'Fornecedores'