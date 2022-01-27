# Generated by Django 3.2 on 2022-01-26 09:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0003_auto_20220125_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='image',
        ),
        migrations.AddField(
            model_name='test',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]