# Generated by Django 3.2 on 2022-01-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0009_auto_20220126_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='post_id',
            field=models.CharField(max_length=36, verbose_name='uuid'),
        ),
    ]
