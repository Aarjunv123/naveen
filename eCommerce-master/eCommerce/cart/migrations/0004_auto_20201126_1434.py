# Generated by Django 3.1.2 on 2020-11-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20201126_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sr_no',
            field=models.SlugField(default=0),
        ),
    ]
