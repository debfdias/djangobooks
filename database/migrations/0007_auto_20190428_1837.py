# Generated by Django 2.1.7 on 2019-04-28 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20190428_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
