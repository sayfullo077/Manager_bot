# Generated by Django 5.0.1 on 2024-03-04 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profile_telegram_id_alter_profile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
