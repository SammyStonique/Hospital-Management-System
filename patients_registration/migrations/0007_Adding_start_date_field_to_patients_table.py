# Generated by Django 4.2 on 2024-03-14 04:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients_registration', '0006_Setting_on_delete_set_null_to_emergency_contact_fk_in_patients_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-start_date']},
        ),
        migrations.AddField(
            model_name='patient',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
