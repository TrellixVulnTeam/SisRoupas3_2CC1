# Generated by Django 2.2.7 on 2019-11-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_remove_roupa_disponivel'),
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='cadastro.Cliente'),
        ),
    ]
