# Generated by Django 4.1.2 on 2022-10-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_accessory_dress'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='img_url',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='img_url',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]
