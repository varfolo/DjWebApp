# Generated by Django 2.1.1 on 2018-12-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20181031_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
