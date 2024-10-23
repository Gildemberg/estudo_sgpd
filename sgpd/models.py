from django.db import models
from django.db.models import CASCADE
from datetime import datetime
from django.db.models import SET_NULL


# Create your models here.



class Etnia(models.Model):
    etn_cod = models.AutoField(primary_key=True)
    etn_descricao = models.CharField(max_length=255)

class Escolaridade(models.Model):
    esc_cod = models.AutoField(primary_key=True)
    esc_descricao = models.CharField(max_length=255)

class Genero(models.Model):
    gen_cod = models.AutoField(primary_key=True)
    gen_descricao = models.CharField(max_length=255)

class OrientacaoSexual(models.Model):
    ori_cod = models.AutoField(primary_key=True)
    ori_descricao = models.CharField(max_length=255)

class Estado(models.Model):
    est_cod = models.AutoField(primary_key=True)
    est_descricao = models.CharField(max_length=255)

class Cidade(models.Model):
    cid_cod = models.AutoField(primary_key=True)
    cid_descricao = models.CharField(max_length=255)

class Endereco(models.Model):
    end_cod = models.AutoField(primary_key=True)
    cid_cod = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    est_cod = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    end_rua = models.CharField(max_length=255)
    end_numero = models.CharField(max_length=6)
    end_complemento = models.CharField(max_length=255)
    end_referencia = models.CharField(max_length=255)

class Area(models.Model):
    are_cod = models.AutoField(primary_key=True)
    are_descricao = models.CharField(max_length=255)
    are_ativo = models.CharField(max_length=1)

class Pessoa(models.Model):
    pes_cod = models.AutoField(primary_key=True)
    pes_nome = models.CharField(max_length=255)
    pes_data_nascimento = models.DateField()
    pes_cpf = models.CharField(max_length=14)
    cid_naturalidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, related_name='naturalidade')
    est_naturalidade = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name='naturalidade')
    end_cod = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    ori_cod = models.ForeignKey(OrientacaoSexual, on_delete=models.SET_NULL, null=True)
    gen_cod = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    esc_cod = models.ForeignKey(Escolaridade, on_delete=models.SET_NULL, null=True)
    etn_cod = models.ForeignKey(Etnia, on_delete=models.SET_NULL, null=True)
    pes_data_ingresso = models.DateField()
    pes_data_egresso = models.DateField()
    pes_ativo = models.CharField(max_length=1)
    are_cod = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)

class AreaPesquisa(models.Model):
    ape_cod = models.AutoField(primary_key=True)
    ape_descricao = models.CharField(max_length=255)

class Bolsista(models.Model):
    bol_cod = models.AutoField(primary_key=True)
    pes_cod = models.ForeignKey(Pessoa, on_delete=CASCADE, null=False)
    bol_data_inicio = models.DateField()
    bol_data_fim = models.DateField()
    bol_ativo = models.CharField(max_length=1)
    ape_cod = models.ForeignKey(AreaPesquisa, on_delete=models.SET_NULL, null=True)

class Cargo(models.Model):
    car_cod = models.AutoField(primary_key=True)
    car_descricao = models.CharField(max_length=255)
    car_ativo = models.CharField(max_length=1)
    are_cod = models.ForeignKey(Area, on_delete=CASCADE, null=False)

class Diretoria(models.Model):
    dir_cod = models.AutoField(primary_key=True)
    pes_cod = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)
    dir_data_inicio = models.DateField()
    dir_data_fim = models.DateField()
    dir_ativo = models.CharField(max_length=1)
    car_cod = models.ForeignKey(Cargo, on_delete=CASCADE, null=False)

class Oficio(models.Model):
    ofi_cod = models.AutoField(primary_key=True)
    ofi_destinatario = models.CharField(max_length=255)
    ofi_assunto = models.CharField(max_length=255)
    ofi_data = models.DateField()
    ofi_texto = models.TextField()
    dir_cod = models.ForeignKey(Diretoria, on_delete=models.SET_NULL, null=True)

class Evento(models.Model):
    eve_cod = models.AutoField(primary_key=True)
    eve_nome = models.CharField(max_length=255)
    eve_local = models.CharField(max_length=255)
    eve_local_saida = models.CharField(max_length=255)
    eve_local_chegada = models.CharField(max_length=255)
    eve_horario_saida = models.TimeField()
    eve_horario_chegada = models.TimeField()
    eve_data = models.DateField()
    eve_local_retorno = models.CharField(max_length=255)
    eve_data_retorno = models.DateField()
    eve_horario_retorno = models.TimeField()

class EventoPessoa(models.Model):
    eve_cod = models.ForeignKey(Evento, on_delete=CASCADE, null=False)
    pes_cod = models.ForeignKey(Pessoa, on_delete=CASCADE, null=False)

class Agenda(models.Model):
    age_cod = models.AutoField(primary_key=True)
    eve_cod = models.ForeignKey(Evento, on_delete=CASCADE, null=True)
    age_data = models.DateField()
    age_descricao = models.CharField(max_length=255)
    age_local = models.CharField(max_length=255)
