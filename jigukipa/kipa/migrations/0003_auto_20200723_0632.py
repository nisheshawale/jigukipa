# Generated by Django 3.0.8 on 2020-07-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kipa', '0002_auto_20200723_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_pic',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]
