# Generated by Django 5.0.1 on 2024-03-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_cakevarient_occassion_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakevarient',
            name='occassion_object',
            field=models.ManyToManyField(to='store.occassion'),
        ),
    ]
