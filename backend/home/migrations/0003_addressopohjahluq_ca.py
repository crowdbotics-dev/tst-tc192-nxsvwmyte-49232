# Generated by Django 2.2.28 on 2022-12-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addressopohjahluq'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressopohjahluq',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
