# Generated by Django 3.2.22 on 2023-11-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bought_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]