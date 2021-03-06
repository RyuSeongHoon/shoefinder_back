# Generated by Django 3.2 on 2022-01-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_name', models.CharField(max_length=256, verbose_name='신발명')),
                ('shoe_brand', models.CharField(max_length=256, verbose_name='브랜드')),
                ('shoe_size', models.CharField(max_length=256, verbose_name='사이즈')),
                ('shoe_color', models.CharField(max_length=256, verbose_name='색깔')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '테스트',
                'verbose_name_plural': '테스트(들)',
            },
        ),
    ]
