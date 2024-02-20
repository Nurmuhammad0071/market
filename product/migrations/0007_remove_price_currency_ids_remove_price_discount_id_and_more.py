# Generated by Django 4.2.9 on 2024-02-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_price_currency_ids_price_discount_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='currency_ids',
        ),
        migrations.RemoveField(
            model_name='price',
            name='discount_id',
        ),
        migrations.AddField(
            model_name='product',
            name='currency_ids',
            field=models.ForeignKey(default=-2024, on_delete=django.db.models.deletion.CASCADE, related_name='prices_by_currency', to='product.currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discount_id',
            field=models.ForeignKey(default=-2024, on_delete=django.db.models.deletion.CASCADE, related_name='prices_by_discount', to='product.discount'),
            preserve_default=False,
        ),
    ]
