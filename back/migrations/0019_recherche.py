# Generated by Django 3.1.3 on 2021-02-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0018_delete_recherche'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recherche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recherche', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
