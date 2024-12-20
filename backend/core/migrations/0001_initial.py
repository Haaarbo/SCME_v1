# Generated by Django 5.1.4 on 2024-12-14 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Outro', max_length=255)),
                ('tipo_material', models.CharField(max_length=255)),
                ('data_validade', models.DateField()),
                ('serial', models.CharField(editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('profissao', models.CharField(max_length=255)),
                ('tipo_usuario', models.CharField(choices=[('Tecnico', 'Técnico'), ('Enfermagem', 'Enfermagem'), ('Administrativo', 'Administrativo')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa', models.CharField(max_length=255)),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.material')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.usuario')),
            ],
        ),
    ]
