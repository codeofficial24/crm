# Generated by Django 4.0.3 on 2022-08-10 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_alter_lead_activity_activity_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='lead_activity',
            name='activity_name',
            field=models.CharField(choices=[('Demo', 'Demo'), ('Follow Up', 'Follow Up'), ('Instalation', 'Instalation')], default='1', max_length=20),
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.catagory')),
            ],
        ),
    ]