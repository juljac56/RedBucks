# Generated by Django 3.1.3 on 2021-01-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0013_tache_fait_par'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='pris',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='pris_par',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='urgent',
            field=models.BooleanField(blank=True),
        ),
    ]
