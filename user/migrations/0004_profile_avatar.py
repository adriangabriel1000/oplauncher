# Generated by Django 5.0.6 on 2024-07-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="profile_pics"),
        ),
    ]
