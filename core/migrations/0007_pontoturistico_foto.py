# Generated by Django 3.0.6 on 2020-05-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]