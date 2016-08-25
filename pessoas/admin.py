from django.contrib import admin

from pessoas.models import Fornecedor,Cliente


admin.site.register(Cliente)
admin.site.register(Fornecedor)