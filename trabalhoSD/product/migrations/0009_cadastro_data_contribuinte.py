# Generated by Django 3.2.5 on 2021-08-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210813_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='data_contribuinte',
            field=models.DateField(null=True, verbose_name='Data Contribuinte'),
        ),
    ]