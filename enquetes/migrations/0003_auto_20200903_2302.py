# Generated by Django 3.1 on 2020-09-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0002_auto_20200903_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquete',
            name='tipo_input',
        ),
        migrations.AlterField(
            model_name='enquete',
            name='data_publicacao',
            field=models.DateField(default='2020-09-03'),
        ),
    ]
