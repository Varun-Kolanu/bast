# Generated by Django 3.2.22 on 2023-11-07 03:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid 10-digit mobile number.')]),
        ),
    ]
