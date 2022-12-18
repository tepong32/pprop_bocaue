# Generated by Django 2.1.5 on 2022-12-18 05:21

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defaults/default.jpg', upload_to=user.models.Profile.dp_directory_path),
        ),
    ]
