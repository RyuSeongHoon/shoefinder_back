# Generated by Django 3.2 on 2022-01-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0010_alter_test_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='post_id',
            new_name='uuid',
        ),
    ]
