# Generated by Django 3.2.4 on 2021-06-22 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_product_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.CharField(max_length=300),
        ),
    ]
