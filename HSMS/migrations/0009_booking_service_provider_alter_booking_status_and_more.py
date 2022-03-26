# Generated by Django 4.0.2 on 2022-03-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HSMS', '0008_booking_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HSMS.service_provider'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Order', 'Order'), ('Pending', 'Pending'), ('Cencel', 'Cencel')], max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HSMS.customer'),
        ),
    ]
