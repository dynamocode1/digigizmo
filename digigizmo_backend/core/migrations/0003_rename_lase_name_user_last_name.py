# Generated by Django 4.2.6 on 2024-05-24 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_email_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lase_name',
            new_name='last_name',
        ),
    ]
