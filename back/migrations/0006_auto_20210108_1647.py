# Generated by Django 3.1.3 on 2021-01-08 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_auto_20210108_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='prenom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back.user'),
        ),
    ]