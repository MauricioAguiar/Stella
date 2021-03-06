# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('cpfCnpq', models.CharField(blank=True, max_length=200, null=True, verbose_name='CPF ou CNPQ')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('cpfCnpq', models.CharField(blank=True, max_length=200, null=True, verbose_name='CPF ou CNPQ')),
                ('endereco_bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco_numero', models.CharField(blank=True, default='S/N', max_length=5, null=True, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_referencia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referência')),
                ('endereco_cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
    ]
