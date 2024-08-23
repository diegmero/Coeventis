# Generated by Django 5.1 on 2024-08-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_company_customuser_nif_customuser_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_provider',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('organizer', 'Organizador'), ('provider', 'Proveedor')], default='organizer', max_length=10),
        ),
    ]
