# Generated by Django 5.0.1 on 2024-03-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_cakevarient_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakevarient',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
