# Generated by Django 3.2.22 on 2023-11-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_user_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
