# Generated by Django 3.2.5 on 2022-02-25 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HSMS', '0005_auto_20220207_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='feature_image',
        ),
    ]