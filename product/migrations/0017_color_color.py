# Generated by Django 4.2.9 on 2024-02-22 13:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_product_text_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
    ]
