# Generated by Django 3.1.3 on 2021-01-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0008_auto_20210109_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='pris',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='titre',
            field=models.CharField(max_length=120),
        ),
    ]
