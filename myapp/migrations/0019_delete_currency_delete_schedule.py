# Generated by Django 5.0.4 on 2024-05-30 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_route_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Currency',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
