# Generated by Django 5.0.1 on 2024-03-04 10:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('97250274-adbd-4aef-bc06-d80d144b8ef8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
