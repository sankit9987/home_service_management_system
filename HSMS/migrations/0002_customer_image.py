# Generated by Django 3.2.5 on 2022-01-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='adhar'),
        ),
    ]
