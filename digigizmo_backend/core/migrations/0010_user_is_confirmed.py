# Generated by Django 4.2.6 on 2024-06-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_cartitem_product_delete_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
