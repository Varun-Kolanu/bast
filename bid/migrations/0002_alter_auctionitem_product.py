# Generated by Django 3.2.22 on 2023-11-05 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_bought_date'),
        ('bid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
