# Generated by Django 4.1.2 on 2022-10-24 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_review_dress_alter_review_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]