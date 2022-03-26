# Generated by Django 3.2.5 on 2022-01-28 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HSMS', '0003_auto_20220128_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=50)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HSMS.service_category')),
            ],
        ),
    ]
