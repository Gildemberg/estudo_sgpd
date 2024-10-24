# Generated by Django 5.1.2 on 2024-10-23 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('are_cod', models.AutoField(primary_key=True, serialize=False)),
                ('are_descricao', models.CharField(max_length=255)),
                ('are_ativo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AreaPesquisa',
            fields=[
                ('ape_cod', models.AutoField(primary_key=True, serialize=False)),
                ('ape_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('cid_cod', models.AutoField(primary_key=True, serialize=False)),
                ('cid_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('esc_cod', models.AutoField(primary_key=True, serialize=False)),
                ('esc_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('est_cod', models.AutoField(primary_key=True, serialize=False)),
                ('est_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('etn_cod', models.AutoField(primary_key=True, serialize=False)),
                ('etn_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('eve_cod', models.AutoField(primary_key=True, serialize=False)),
                ('eve_nome', models.CharField(max_length=255)),
                ('eve_local', models.CharField(max_length=255)),
                ('eve_local_saida', models.CharField(max_length=255)),
                ('eve_local_chegada', models.CharField(max_length=255)),
                ('eve_horario_saida', models.TimeField()),
                ('eve_horario_chegada', models.TimeField()),
                ('eve_data', models.DateField()),
                ('eve_local_retorno', models.CharField(max_length=255)),
                ('eve_data_retorno', models.DateField()),
                ('eve_horario_retorno', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('gen_cod', models.AutoField(primary_key=True, serialize=False)),
                ('gen_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrientacaoSexual',
            fields=[
                ('ori_cod', models.AutoField(primary_key=True, serialize=False)),
                ('ori_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('car_cod', models.AutoField(primary_key=True, serialize=False)),
                ('car_descricao', models.CharField(max_length=255)),
                ('car_ativo', models.CharField(max_length=1)),
                ('are_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgpd.area')),
            ],
        ),
        migrations.CreateModel(
            name='Diretoria',
            fields=[
                ('dir_cod', models.AutoField(primary_key=True, serialize=False)),
                ('dir_data_inicio', models.DateField()),
                ('dir_data_fim', models.DateField()),
                ('dir_ativo', models.CharField(max_length=1)),
                ('car_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgpd.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('end_cod', models.AutoField(primary_key=True, serialize=False)),
                ('end_rua', models.CharField(max_length=255)),
                ('end_numero', models.CharField(max_length=6)),
                ('end_complemento', models.CharField(max_length=255)),
                ('end_referencia', models.CharField(max_length=255)),
                ('cid_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.cidade')),
                ('est_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('age_cod', models.AutoField(primary_key=True, serialize=False)),
                ('age_data', models.DateField()),
                ('age_descricao', models.CharField(max_length=255)),
                ('age_local', models.CharField(max_length=255)),
                ('eve_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sgpd.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('ofi_cod', models.AutoField(primary_key=True, serialize=False)),
                ('ofi_destinatario', models.CharField(max_length=255)),
                ('ofi_assunto', models.CharField(max_length=255)),
                ('ofi_data', models.DateField()),
                ('ofi_texto', models.TextField()),
                ('dir_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.diretoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pes_cod', models.AutoField(primary_key=True, serialize=False)),
                ('pes_nome', models.CharField(max_length=255)),
                ('pes_data_nascimento', models.DateField()),
                ('pes_cpf', models.CharField(max_length=14)),
                ('pes_data_ingresso', models.DateField()),
                ('pes_data_egresso', models.DateField()),
                ('pes_ativo', models.CharField(max_length=1)),
                ('are_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.area')),
                ('cid_naturalidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='naturalidade', to='sgpd.cidade')),
                ('end_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.endereco')),
                ('esc_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.escolaridade')),
                ('est_naturalidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='naturalidade', to='sgpd.estado')),
                ('etn_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.etnia')),
                ('gen_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.genero')),
                ('ori_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.orientacaosexual')),
            ],
        ),
        migrations.CreateModel(
            name='EventoPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eve_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgpd.evento')),
                ('pes_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgpd.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='diretoria',
            name='pes_cod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.pessoa'),
        ),
        migrations.CreateModel(
            name='Bolsista',
            fields=[
                ('bol_cod', models.AutoField(primary_key=True, serialize=False)),
                ('bol_data_inicio', models.DateField()),
                ('bol_data_fim', models.DateField()),
                ('bol_ativo', models.CharField(max_length=1)),
                ('ape_cod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgpd.areapesquisa')),
                ('pes_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgpd.pessoa')),
            ],
        ),
    ]
