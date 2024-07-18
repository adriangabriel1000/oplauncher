# Generated by Django 5.0.6 on 2024-07-17 09:03

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.FileField(
                blank=True, null=True, upload_to=user.models.get_image_name
            ),
        ),
    ]
