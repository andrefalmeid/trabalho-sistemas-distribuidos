# Generated by Django 3.2.5 on 2021-08-06 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_livroartigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livroartigo',
            name='ciclo_de_vida',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.ciclo_de_vida'),
        ),
        migrations.AlterField(
            model_name='livroartigo',
            name='geral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.geral'),
        ),
        migrations.AlterField(
            model_name='livroartigo',
            name='meta_metadados',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.meta_metadados'),
        ),
    ]
