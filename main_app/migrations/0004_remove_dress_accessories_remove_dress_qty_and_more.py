# Generated by Django 4.1.2 on 2022-10-21 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_dress_accessories_dress_qty_alter_dress_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dress',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='dress',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='dress',
            name='user',
        ),
    ]
