from django.db import models



class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=200, verbose_name=u'Nome', null=False, blank=False)
    email = models.EmailField(max_length=200, verbose_name=u'E-mail', null=True, blank=True)
    cpfCnpq = models.CharField(max_length=200, verbose_name=u'CPF ou CNPQ', null=True, blank=True)

    # Endereço
    endereco_bairro = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Bairro')
    endereco_numero = models.CharField(max_length=5, default=u'S/N', null=True, blank=True, verbose_name=u'Número')
    endereco_complemento = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Complemento')
    endereco_referencia = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Referência')
    endereco_cidade = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Cidade')
    endereco_estado = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Estado')

    def __str__(self):
        return self.nome