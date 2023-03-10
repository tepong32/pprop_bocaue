# Generated by Django 2.1.5 on 2022-12-16 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=70)),
                ('m_name', models.CharField(max_length=70)),
                ('l_name', models.CharField(max_length=70)),
                ('address', models.CharField(default='Bocaue, Bulacan', max_length=70)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Select', 'Select')], default='Select', max_length=10)),
                ('image', models.ImageField(default='default.jpg', upload_to=user.models.Profile.dp_directory_path)),
                ('user_loc', models.CharField(choices=[('Antipona', 'Antipona'), ('Bagumbayan', 'Bagumbayan'), ('Bambang', 'Bambang'), ('Batia', 'Batia'), ('Biñang 1st', 'Biñang_1st'), ('Biñang 2nd', 'Biñang_2nd'), ('Bolacan', 'Bolacan'), ('Bundukan', 'Bundukan'), ('Bunlo', 'Bunlo'), ('Caingin', 'Caingin'), ('Duhat', 'Duhat'), ('Igulot', 'Igulot'), ('Lolomboy', 'Lolomboy'), ('Poblacion', 'Poblacion'), ('Sulucan', 'Sulucan'), ('Taal', 'Taal'), ('Tambobong', 'Tambobong'), ('Turo', 'Turo'), ('Wakas', 'Wakas'), ('Select', 'Select')], default='Select', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
