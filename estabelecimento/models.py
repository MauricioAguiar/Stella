from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from pessoas.models import Fornecedor, Cliente


class Produto(models.Model):

    nome = models.CharField(max_length=200, verbose_name=u'Nome', null=False, blank=False)
    preco_venda = models.DecimalField(verbose_name=u'Preço do produto', max_digits=7, decimal_places=2)
    quantidade = models.IntegerField(verbose_name=u'Quantidade', default=0, null=False, blank=False)
    desconto = models.IntegerField(verbose_name=u'Porcentagem de desconto', default=0, null=False, blank=False, help_text=u'Aqui você pode colocar um valor padrão de desconto sobre uma peça deste estabelecimento')
    onDesconto = models.BooleanField(verbose_name=u'Ativar desconto?', default=0, null=False, blank=False, help_text=u'Aqui você tem a opção de ativar ou desativar o desconto')


    def __str__(self):
        return self.nome


class CtrlEstoque(models.Model):

    class Meta:
        verbose_name = u'Fazer reposição'
        verbose_name_plural = u'Fazer reposições'

    fornecedor = models.ForeignKey(Fornecedor, verbose_name=u'Fornecedor')
    data_aquisicao = models.DateField(auto_now_add=True, verbose_name=u'Data da aquisição')
    produto = models.ForeignKey(Produto, verbose_name=u'Produto')
    preco_compra = models.DecimalField(verbose_name=u'Valor da compra por unidade', max_digits=7, decimal_places=2)
    quantidade = models.IntegerField(verbose_name=u'Quantidade', default=0, null=False, blank=False)


    def save(self, *args, **kwargs):

        produto = Produto.objects.get(pk=self.produto.pk)

        produto.quantidade += self.quantidade
        produto.save()
        super(CtrlEstoque, self).save(*args, **kwargs)



    def __str__(self):
        return self.fornecedor.nome

class Pedido(models.Model):

    class Meta:
        verbose_name = u'Compra'

    desconto = models.IntegerField(verbose_name=u'Desconto', default=0, null=False, blank=False)
    cliente = models.ForeignKey(Cliente)
    #Auto-Inserts

    data_venda = models.DateField(auto_now_add=True, verbose_name=u'Data da Venda')



class AddProduto(models.Model):

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'


    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido)


    quantidade = models.PositiveIntegerField(verbose_name=u'Quantidade', default=1, null=False, blank=False)

    def save(self, *args, **kwargs):

        produto = Produto.objects.get(pk=self.produto.pk)

        produto.quantidade -= self.quantidade
        produto.save()
        super(AddProduto, self).save(*args, **kwargs)



class Servico(models.Model):

    class Meta:
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'

    descricao = models.CharField(max_length=200, verbose_name=u'Descrição', null=False, blank=False)
    preco_servico = models.DecimalField(verbose_name=u'Valor do serviço', max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=200, verbose_name=u'Tipo do serviço', null=False, blank=False)
    data_entrega = models.DateField(verbose_name=u'Data de entrega')
    quantidade = models.IntegerField(verbose_name=u'Quantidade', default=1, null=True, blank=True)
    pedido = models.ForeignKey(Pedido)

    def __str__(self):
        return self.tipo

