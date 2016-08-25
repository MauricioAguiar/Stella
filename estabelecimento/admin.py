from django.contrib import admin
from estabelecimento.models import *

class ServicoInline(admin.TabularInline):
    model=Servico
    extra= 0


class ProdutoInline(admin.TabularInline):
    model=AddProduto
    extra= 0


class PedidoAdmin(admin.ModelAdmin):
    list_display=['cliente', 'data_venda']
    inlines = [ServicoInline, ProdutoInline]

class CtrlEstoqueAdmin(admin.ModelAdmin):
    list_display=['fornecedor', 'data_aquisicao', 'produto']
    list_filter=['data_aquisicao']

admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(CtrlEstoque, CtrlEstoqueAdmin)
admin.site.register(Servico)