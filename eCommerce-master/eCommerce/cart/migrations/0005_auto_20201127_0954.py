# Generated by Django 3.1.2 on 2020-11-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20201126_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sr_no',
            field=models.SlugField(unique=True),
        ),
    ]