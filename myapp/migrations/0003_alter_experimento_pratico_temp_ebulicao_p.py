# Generated by Django 4.2 on 2023-06-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_experimento_teorico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimento_pratico',
            name='temp_ebulicao_p',
            field=models.FloatField(default=None),
        ),
    ]
