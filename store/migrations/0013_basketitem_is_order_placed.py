# Generated by Django 5.0.1 on 2024-03-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_basketitem_weight_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
    ]
