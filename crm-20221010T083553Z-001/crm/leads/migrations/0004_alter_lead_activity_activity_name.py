# Generated by Django 4.0.3 on 2022-08-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_lead_communication_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead_activity',
            name='activity_name',
            field=models.CharField(choices=[('Demo', 'Demo'), ('Instalation', 'Instalation')], default='1', max_length=20),
        ),
    ]