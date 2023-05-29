# Generated by Django 4.2.1 on 2023-05-29 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_brand'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='variation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.productvariation'),
            preserve_default=False,
        ),
    ]
