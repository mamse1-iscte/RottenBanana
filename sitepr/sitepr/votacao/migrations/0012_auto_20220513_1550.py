# Generated by Django 3.2.12 on 2022-05-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0011_auto_20220509_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme_ou_serie',
            name='filme_ranking_audiencia',
        ),
        migrations.AlterField(
            model_name='filme_ou_serie',
            name='filme_ranking_critica',
            field=models.FloatField(default=0),
        ),
    ]
