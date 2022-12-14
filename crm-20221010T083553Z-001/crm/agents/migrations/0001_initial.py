# Generated by Django 4.0.3 on 2022-07-26 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('agent_name', models.CharField(max_length=20)),
                ('organisation', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50, null=True)),
            ],
        ),
    ]
