# Generated by Django 3.2 on 2022-01-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0004_auto_20220126_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shoe_images'),
        ),
    ]
